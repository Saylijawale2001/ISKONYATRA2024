from django.contrib import messages
from django.db import connection
from ISKON_yatra2024 import settings
from django.db import IntegrityError
from django.shortcuts import render, redirect, HttpResponse
from .models import mar24yatra_reg,yatrauser
def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phoneNumber')
        password = request.POST.get('password')

        # Check if the user exists in the yatrauser table
        user = yatrauser.objects.filter(phone_number=phone_number, password=password).first()

        if user:
            # User exists, redirect to the home page or any other page you want
            # For now, redirecting to the 'customerhome' page
            return redirect('customerhome')
        else:
            # User doesn't exist, show an error message
            messages.error(request, 'Invalid login credentials. Please try again or register.')

    return render(request, 'login.html')

def customer_home_view(request):
    return render(request, 'customerhome.html')


def CustRegistrationView(request):
    if request.method == 'POST':
        # Handle form submission
      try:
         registration_data = {
            'fR_Name': request.POST.get('name'),
            'fR_age': request.POST.get('age'),
            'fR_gender': request.POST.get('gender'),
            'fR_Mob': request.POST.get('contact'),
            'fR_chant': request.POST.get('chanting'),
            'consellor_Name': request.POST.get('counsellor'),
            'no_of_Rooms': request.POST.get('room'),
            'room_cost': request.POST.get('cost'),
            'yatra_type': request.POST.get('yatra'),
            'travelling_From': request.POST.get('city'),
            'transport_Mode': request.POST.get('onward'),
            'coach_number': request.POST.get('return'),
            'return_Transport_Mode': request.POST.get('return'),
            'return_coach_number': request.POST.get('return'),
            'any_Comments': request.POST.get('special'),
            'm1_name': request.POST.get('name1', ''),
            'm1_age': request.POST.get('age1',''),
            'm1_gender': request.POST.get('gender1',''),
            'm2_name': request.POST.get('name1',''),
            'm2_age': request.POST.get('age1',''),
            'm2_gender': request.POST.get('gender1',''),
            'm3_name': request.POST.get('name1',''),
            'm3_age': request.POST.get('age1',''),
            'm3_gender': request.POST.get('gender1',''),
            'm4_name': request.POST.get('name1',''),
            'm4_age': request.POST.get('age1',''),
            'm4_gender': request.POST.get('gender1',''),
            'm5_name': request.POST.get('name1',''),
            'm5_age': request.POST.get('age1',''),
            'm5_gender': request.POST.get('gender1',''),
            'm6_name': request.POST.get('name1',''),
            'm6_age': request.POST.get('age1',''),
            'm6_gender': request.POST.get('gender1',''),
            'm7_name': request.POST.get('name1',''),
            'm7_age': request.POST.get('age1',''),
            'm7_gender': request.POST.get('gender1',''),
          }
         yatrausersdict ={
         'fR_Name': request.POST.get('name'),
         'fR_Mob': request.POST.get('contact'),
         'password': request.POST.get('contact'),
         'role': 'client',
         'client_id': '',}
         for i in range(1, 8):
             member_name = request.POST.get(f'name{i}', '')
             member_age = request.POST.get(f'age{i}', '')
             member_gender = request.POST.get(f'gender{i}', '')

             if member_name or member_age or member_gender:
                 registration_data[f'm{i}_name'] = member_name
                 registration_data[f'm{i}_age'] = member_age
                 registration_data[f'm{i}_gender'] = member_gender

         """# Construct the SQL query
         mar24yatra_reg.objects.create(**registration_data)"""
         with connection.cursor() as cursor:
             query = "INSERT INTO mar24yatra_reg ({}) VALUES ({})"
             fields = ", ".join(registration_data.keys())
             values = ", ".join(["%s"] * len(registration_data))
             query = query.format(fields, values)
             cursor.execute(query, list(registration_data.values()))

             query = """INSERT INTO yatrauser (name, phone_number, password, role, client_id) VALUES (%s, %s, %s, 
             %s,%s) """
             cursor.execute(query, [yatrausersdict['fR_Name'], yatrausersdict['fR_Mob'],
                                    yatrausersdict['password'], yatrausersdict['role'],yatrausersdict['client_id']])

      except IntegrityError as e:
        print(f"Error inserting data into the database: {e}")
        # Redirect to a success page or any other logic
        print(registration_data)
    return render(request, 'custregistration.html')

        # Redirect to a success page or any other logic
