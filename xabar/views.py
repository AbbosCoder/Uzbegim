# from django.shortcuts import render, redirect
# from django.views import View
# from .forms import XabarForm
# from .utils import send_telegram_message  # Assuming utility is in utils.py

# # Bot token and chat ID - should be stored securely in environment variables or settings


# class ContactView(View):
#     template_name = 'contact.html'

#     def get(self, request):
#         form = XabarForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = XabarForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form to the database
#             # Compose a message to send to Telegram
#             xabar = form.instance
#             telegram_message = f"New message from {xabar.name}.\nEmail: {xabar.email}\nPhone: {xabar.phone_number}\nMessage: {xabar.message}"

#             # Send the message to Telegram
#             status, response = send_telegram_message(telegram_message)

#             if status == 200:
#                 print("Message sent to Telegram successfully")
#             else:
#                 print("Failed to send message to Telegram:", response)

#             return redirect('contact')  # Redirect after submission
#         return render(request, self.template_name, {'form': form})
