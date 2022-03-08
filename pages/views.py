from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): # new
    template_name = 'About.html'


class RAMPageView(TemplateView): # new
    template_name = 'pages/RAM.html'


class CpuPageView(TemplateView): # new
    template_name = 'pages/cpu.html'


class PsuPageView(TemplateView): # new
    template_name = 'pages/psu.html'


class GpuPageView(TemplateView): # new
    template_name = 'pages/gpu.html'


class MboardPageView(TemplateView): # new
    template_name = 'pages/motherboard.html'