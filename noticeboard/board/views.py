import mimetypes
from django.db.models import Q
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notice
from board.forms import NoticeForm


class NoticeListView(ListView):
    model = Notice
    template_name = 'notice_list.html'
    context_object_name = 'notices'
    paginate_by = 9
    
    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            # Perform case-insensitive search by title
            return Notice.objects.filter(Q(title__icontains=query)).order_by('-created_at')
        else:
            return Notice.objects.all().order_by('-created_at')
    


class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notice_detail.html'
    context_object_name = 'notice'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get notices of the same category, excluding the current notice
        category_notices = Notice.objects.filter(category=self.object.category).exclude(id=self.object.id)[:3]

        context['category_notices'] = category_notices
        return context
    
    

class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    login_url = '/login/'
    redirect_field_name = 'notice_detail.html'
    template_name = 'notice_form.html'
    form_class = NoticeForm
    success_url = reverse_lazy('notice_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        if form.is_valid():
            return super().form_valid(form)
        else:
            # Handle form validation errors
            return self.form_invalid(form)
        
class NoticeUpdateView(LoginRequiredMixin, UpdateView):
    model = Notice
    template_name = 'notice_form.html'
    login_url = '/login/'
    redirect_field_name = 'notice_detail.html'
    form_class = NoticeForm
    success_url = reverse_lazy('notice_list')
    
    def get_success_url(self):
        return reverse_lazy('notice_detail', args=[self.object.id]) 

class NoticeDeleteView(LoginRequiredMixin, DeleteView):
    model = Notice
    template_name = 'notice_confirm_delete.html'
    success_url = reverse_lazy('notice_list')
    

class FileDownloadView(View):
    def get(self, request, pk):
        notice = get_object_or_404(Notice, pk=pk)

        # Assuming 'file' is the field storing the file in your model
        file_path = notice.file.path if notice.file else None

        if file_path:
            with open(file_path, 'rb') as file:
                content_type, _ = mimetypes.guess_type(file_path)
                if content_type is None:
                    content_type = 'application/octet-stream'
                
                response = HttpResponse(file.read(), content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename={notice.title}_file{mimetypes.guess_extension(content_type)}'
                return response
        else:
            return HttpResponse("File not found", status=404)
        
        
        
