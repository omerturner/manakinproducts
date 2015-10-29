from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from .forms import ContactForm
from .models import WebsiteContact
# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            subject = request.POST.get('subject', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            
            # Email the profile with the 
            # contact information
            template = get_template('contact/contact_template.txt')
            context = Context({
                'subject': subject,
                'email': email,
                'message': message,
            })
            content = template.render(context)

            email_message = EmailMessage(
                "New contact form submission",
                content,
                "manakinproducts.com" +'<support@manakinproducts.com>',
                ['manakingproducts@gmail.com'],
                headers = {'Reply-To': email }
            )
            email_message.send()
            WebsiteContact(subject=subject,email=email,message=message).save()
            return redirect('sent')

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })









