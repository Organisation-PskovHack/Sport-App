from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from section.models import Section, UserSection


class homePage(TemplateView):
    template_name = "page/home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ScanQR(TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_student:
                return redirect(f"/profile/{request.user.id}/")
        except Exception as e:
            print(e)
            return redirect("/login")
        return super().get(request, *args, **kwargs)

    def post(self, request):
        student = request.POST.get("student")
        section = Section.objects.get(user_id=request.user.id)
        # TODO: Доделать открытие/закрытие тренировки
        return HttpResponse("Hello world!")  # Заглушка


class SectionList(ListView):
    model = Section
    template_name = 'page/section_list.html'


class SectionDetail(DetailView):
    model = Section
    template_name = "page/section_detail.html"

    def __init__(self):
        self.user = None
        self.pk = None

    def get(self, request, pk, *args, **kwargs):
        self.pk = pk
        try:
            if request.user.is_student:
                self.user = request.user
        except Exception as e:
            print(e)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SectionDetail, self).get_context_data()
        if self.user:
            if UserSection.objects.get(user_id=self.user.id, section_id=self.pk):
                context["subscribe"] = False
            else:
                context["subscribe"] = True
        else:
            context["subscribe"] = True
        return context
