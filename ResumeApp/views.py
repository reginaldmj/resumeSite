from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView): # index / home page
	template_name = "ResumeApp/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context


class ContactView(generic.FormView): # contact url page
	template_name = "ResumeApp/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView): # portfolio page
	model = Portfolio
	template_name = "ResumeApp/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView): # portfolio view page
	model = Portfolio
	template_name = "ResumeApp/portfolio-detail.html"

class BlogView(generic.ListView): # blog view page
	model = Blog
	template_name = "ResumeApp/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView): # blog details page
	model = Blog
	template_name = "ResumeApp/blog-detail.html"