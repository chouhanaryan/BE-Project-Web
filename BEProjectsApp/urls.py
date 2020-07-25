from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf.urls import url
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from BEProjectsApp import views


# app_name = "BEProjectsApp"
router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet)
router.register(r"teachers", views.TeacherViewSet)
router.register(r"contributors", views.ContributorViewSet)
# router.register(r"contributors-url",views.ContributorUrlViewSet)

# SchemaView
schema_view = get_swagger_view(title="BEProjects")


urlpatterns = [
    url(r"^api/", include((router.urls, "api"))),
    url(r"^api/search/", views.SearchProjectView.as_view(), name="search"),
    url(r"^schema/$", schema_view),
    url(r"^api/get_domains/$", views.GetDomainView.as_view(), name="domain"),
    path("api/Approve_project", views.Approve.as_view(), name="Approve Project"),
    path("api/Login", views.Login.as_view(), name="Login"),
    path("api/Delete_Project", views.Delete_Project.as_view(), name="Delete_Project"),
    path(
        "api/create_project",
        views.CreateProjectWithContributors.as_view(),
        name="Create_Project_with_Contributors",
    ),
]

urlpatterns += router.get_urls()
