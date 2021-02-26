import datetime

from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from account.models import User
from section.models import Section, UserSection, Workout


class homePage(TemplateView):
    template_name = "page/home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ScanQR(DetailView):
    model = Section
    template_name = "page/scan.html"
    context_object_name = "work"

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_student:
                return redirect(f"/profile/{request.user.id}/")
        except Exception as e:
            print(e)
            return redirect("/login")
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ScanQR, self).get_context_data()
        work_id = self.kwargs['work']
        context["users"] = Workout.objects.filter(workout_id=int(work_id))
        return context

    def post(self, request, **kwargs):
        action = request.POST.get("action")
        work_id = int(self.kwargs['work'])
        if action == "start":
            student = request.POST.get("student")
            # section = Section.objects.get(user_id=request.user.id)
            try:
                workout = Workout()
                workout.workout_id = work_id
                workout.user_id = int(student)
                t = datetime.datetime.now().time()
                workout.start_time = t
                workout.end_time = t
                workout.date = str(datetime.date.today())
                workout.save()
                return redirect(f"/section/{int(self.kwargs['pk'])}/scan/{work_id}/")
            except Exception as e:
                print(e)
        elif action == "end":
            student = request.POST.get("student")
            workout = Workout.objects.get(user_id=int(student))
            workout.end_time = datetime.datetime.now().time()
            workout.save()
            return redirect(f"/section/{self.kwargs['pk']}/{work_id}/")
        return HttpResponse("invalid data")  # Заглушка


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
        context["subscribers"] = len(UserSection.objects.filter(section_id=self.pk))
        if self.user:
            try:
                if UserSection.objects.get(user_id=self.user.id, section_id=self.pk):
                    context["subscribe"] = False
                else:
                    context["subscribe"] = True
            except:
                context["subscribe"] = True
        else:
            context["subscribe"] = True
        context["user"] = User.objects.get(id=self.get_object().user_id)
        return context

    def post(self, request, pk):
        action = request.POST.get("action")
        if action == "subscribe":
            section = pk
            user = request.user
            user_section = UserSection()
            user_section.section_id = section
            user_section.user_id = user.id
            user_section.save()
        elif action == "unsub":
            UserSection.objects.get(section_id=pk, user_id=request.user.id).delete()

        return redirect(f"/section/{pk}/")

<<<<<<< Updated upstream
class TestSectionDetail(TemplateView):
    template_name = "page/section_detail.html"


class DataTable(TemplateView):
    template_name = "page/dataTable.html"
=======
>>>>>>> Stashed changes
