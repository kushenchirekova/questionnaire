"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from things.views import StudentLoginView,TestInfoView,TestView

import things.views as views

from things.admin_views.views import (
    RegistrationView, LoginView, LogoutView,
    HomeView, AdminTestListView, AdminTestCreateView,
    AdminTestDetailView, StudentResultDetailView,
    PreActivationView, ActivationView,
    StudentListView, StudentDetailView,
    StudentCreateView, StudentCreateSuccess,
    StudentDeleteView, TestDeleteView, CsvImportMessageView,
    StudentEditView, TestEditView, AdminTestUpdateView,
    TestStudentAddView, TestEditStudentsView,
    copy_test, admin_question_delete, share_test,
    student_csv_import, admin_question_update, admin_test,
    filter_students, students_results, check_speciality,
    admin_test_edit, questions_csv_import, ajax_question_create,
    initial
)

urlpatterns = [
    path('superuser/', admin.site.urls),
    path('Test/<int:user_id>/result/',views.result, name='res'),
    path('Test/<int:user_id>/identification/',views.checkStudent, name='check'),
    path('Test/<int:user_id>/',TestView.as_view(),name='test'),
    path('',StudentLoginView.as_view(),name="reg1"),
    path('TestInfo/<id>',TestInfoView.as_view(),name='reg3'),
    # path('notAvailable/<id>',views.no,name="notAvailable"),
    # path('Cannot/<id>',views.cannot,name="Cannot"),
#----------------------------
    path('', initial, name='admin-initial'),
    path('admin/register/', RegistrationView.as_view(), name='admin-registration'),
    path('admin/login/', LoginView.as_view(), name='admin-login'),
    path('admin/logout/', LogoutView.as_view(), name='admin-logout'),
    path('admin/pre-activate/', PreActivationView.as_view(), name='admin-pre-activation'),
    path('admin/activate/<uidb64>/<token>/', ActivationView.as_view(), name='admin-activation'),
    path('admin/home/', HomeView.as_view(), name='admin-home'),
    path('admin/tests/', AdminTestListView.as_view(), name='admin-tests'),
    path('admin/tests/create/', AdminTestCreateView.as_view(), name='admin-create-test'),
    path('admin/tests/<int:test_id>/create/', AdminTestUpdateView.as_view(), name='admin-update-test'),
    path('admin/tests/<int:test_id>/questions/', admin_test, name='admin-test'),
    path('admin/tests/<int:test_id>/questions/csv', questions_csv_import, name='admin-import-questions-csv'),
    path('admin/tests/<int:test_id>/groups/', TestStudentAddView.as_view(),
         name='admin-test-add-students'),
    path('admin/tests/<int:test_id>/share/', share_test, name='admin-share-test'),
    path('admin/testid<uidb64>/', filter_students, name='admin-filter-students'),
    path('admin/tests/<int:test_id>/', AdminTestDetailView.as_view(),
         name='admin-test-details'),
    path('admin/tests/<int:test_id>/edit/', TestEditView.as_view(), name='admin-edit-test'),
    path('admin/tests/<int:test_id>/edit/questions/', admin_test_edit, name='admin-edit-questions'),
    path('admin/tests/<int:test_id>/edit/groups/', TestEditStudentsView.as_view(),
         name='admin-test-edit-students'),
    path('admin/tests/<int:test_id>/delete/', TestDeleteView.as_view(), name='admin-delete-test'),
    path('admin/tests/<int:test_id>/copy/', copy_test, name='admin-copy-test'),
    path('admin/tests/<int:test_id>/result/<int:result_id>/', StudentResultDetailView.as_view(),
         name='admin-student-result'),
    path('admin/students/', StudentListView.as_view(), name='admin-students'),
    path('admin/students/<int:student_id>/', StudentDetailView.as_view(), name='admin-student-details'),
    path('admin/students/create/', StudentCreateView.as_view(), name='admin-create-student'),
    path('admin/students/create/csv/', student_csv_import, name='admin-create-student-csv'),
    path('admin/students/create/success/', StudentCreateSuccess.as_view(), name='admin-create-student-success'),
    path('admin/students/csvimport/result/', CsvImportMessageView.as_view(), name='admin-csv-message-view'),
    path('admin/students/<int:student_id>/delete/', StudentDeleteView.as_view(), name='admin-delete-student'),
    path('admin/students/<int:student_id>/edit/', StudentEditView.as_view(), name='admin-edit-student'),

    # ajax
    path('questions/<int:question_id>/delete', admin_question_delete, name='admin-delete-question'),
    path('admin/tests/<int:test_id>/questions/<int:question_id>/update', admin_question_update,
         name='admin-question-update'),
    path('ajax/tests/<int:test_id>/<str:sort_by>', students_results, name='admin-details-students'),
    path('ajax/speciality', check_speciality, name='admin-check-speciality'),

    path('ajax/questions/create', ajax_question_create, name='ajax-question-create')
    # ajax
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
