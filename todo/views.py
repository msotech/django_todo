from django.shortcuts import redirect

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status

from todo.forms import ToDoForm
from todo.models import ToDo
from todo.serializers import ToDoSerializer


class ToDoCreateListView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = "todo/todo_listcreate.html"
    form_class = ToDoForm

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)

        if request.accepted_renderer.format == "html":
            if request.path == "/todos/":
                return redirect("home")

            form_data = self.form_class()
            return Response({"todos": serializer.data, "form": form_data})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            form = self.form_class(request.POST)

            if form.is_valid():
                form.save()

                return redirect("home")

            serializer = self.serializer_class(self.get_queryset(), many=True)

            return Response(
                {"todos": serializer.data, "form": form},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class ToDoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = "todo/todo_detail.html"
    form_class = ToDoForm

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())

        if request.accepted_renderer.format == "html":
            if request.GET.get("confirm_delete"):
                return Response(
                    {"todo": serializer.data},
                    template_name="todo/todo_delete.html",
                )

            form = self.form_class(instance=self.get_object())
            return Response({"todo": serializer.data, "form": form})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.accepted_renderer.format == "html":
            form = self.form_class(request.POST, instance=self.get_object())

            if form.is_valid():
                form.save()

                return redirect("home")

            serializer = self.serializer_class(self.get_object())
            return Response(
                {"todo": serializer.data, "form": form},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)