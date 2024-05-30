import logging
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, View, ListView
from itertools import chain
from team.models import RoadRegistration

from .models import Content, WatchedContent, Road

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class Roads(LoginRequiredMixin, View):
    template_name = "content/roads.html"
    context = {"title":"مسیرهای آموزشی"}

    def get(self, request):
        user = request.user
        try:
            # Retrieve roads registered by the user
            user_roads = user.user_of_road_registration.all()
            # Retrieve roads registered by teams the user is a member of
            team_roads = []
            for team in user.members_of_team.all():
                team_roads.extend(team.team_of_road_registration.all())
            # Convert team_roads to a queryset
            team_roads_queryset = RoadRegistration.objects.filter(id__in=[road.id for road in team_roads])
            # Combine user roads and team roads into a single queryset
            all_roads = user_roads | team_roads_queryset
            # Ensure uniqueness of roads using distinct() queryset method
            unique_roads = all_roads.distinct()

            self.context["active_roads"] = unique_roads.filter(status="a")
            self.context["requested_roads"] = unique_roads.exclude(status='a')
            self.context["roads"] = Road.objects.all()
        except AttributeError as e:
            logging.error("An AttributeError occurred: %s", e)

        return render(request, self.template_name, self.context)
    

class RoadDetail(LoginRequiredMixin, DetailView):
    model = Road
    template_name = "content/road.html"
    slug_field, slug_url_kwarg = "uuid", "uuid"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "مسیر آموزشی"
        context["watched_list"] = WatchedContent.objects.filter(user=self.request.user).values_list('content__uuid', flat=True)

        collections = self.get_object().road_of_collection_order.all()
        steps = []
        for col_ord in collections:
            contents = col_ord.collection.collection_of_content_order.all()
            exams = col_ord.collection.collection_of_exam_order.all()
            tasks = col_ord.collection.collection_of_task_order.all()
            collection_steps = sorted(chain(contents, exams, tasks), key=lambda x: x.row_number)
            steps.extend(collection_steps)
        context["collections"] = collections
        context["steps"] = sorted(steps, key=lambda x: x.row_number)
        context["steps"] = steps
        return context


class ContentDetail(LoginRequiredMixin, DetailView):
    model = Content
    template_name = "content/detail.html"
    slug_field, slug_url_kwarg = "uuid", "uuid"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"{self.get_object().title}"
        return context


@login_required
def user_watched_content(request, content_uuid):
    content = get_object_or_404(Content, uuid=content_uuid)
    WatchedContent.objects.create(user=request.user, content=content)

    if content.medals:
        request.user.received_medals = (request.user.received_medals or 0) + content.medals
        request.user.save()

    return redirect("content:roads")


class FundsManagements(LoginRequiredMixin, View):
    template_name = "content/funds-management.html"
    context = {"title":"مدیریت صندوق ها"}

    def get(self, request):
        return render(request, self.template_name, self.context)