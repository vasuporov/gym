from django.shortcuts import render, redirect
from django.views.generic import View
import datetime
import pytz
from models import *
import forms
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import os
from django.views.generic import ListView


@login_required()
def home(request):
    # fetch the current fees structure for display
    gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
    fees_structures = FeesStructure.objects.filter(gym=gym).all()

    # adding some required data to the session which will be needed on many views
    request.session['gym_name'] = gym.gym_name

    # fetch the list of member so that user can select which one to delete
    members = GymMember.objects.filter(gym=gym)

    return render(request, "home.html", {"fees_structures": fees_structures, "members": members})


class CreateGymMember(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
            add_member_form = forms.AddGymMemberForm(gym, initial={"joining_date": datetime.datetime.today().date()})

            return render(request, "add_gym_member.html", {"add_member_form": add_member_form})
        return redirect('/accounts/login')

    def post(self, request):
        if request.user.is_authenticated():
            # get the gym of gym owner
            gym = Gym.objects.filter(gym_owner_id=request.user.id).first()

            add_member_form = forms.AddGymMemberForm(gym, request.POST, request.FILES)

            if add_member_form.is_valid():
                try:
                    first_name = add_member_form.cleaned_data["first_name"]
                    last_name = add_member_form.cleaned_data["last_name"]
                    gender = add_member_form.cleaned_data["gender"]
                    date_of_birth = add_member_form.cleaned_data["date_of_birth"]
                    phone = add_member_form.cleaned_data["phone"]
                    photo = add_member_form.cleaned_data["photo"]
                    height = add_member_form.cleaned_data["height"]
                    weight = add_member_form.cleaned_data["weight"]
                    biceps_right = add_member_form.cleaned_data["biceps_right"]
                    biceps_left = add_member_form.cleaned_data["biceps_left"]
                    triceps_right = add_member_form.cleaned_data["triceps_right"]
                    triceps_left = add_member_form.cleaned_data["triceps_left"]
                    fees_structure = add_member_form.cleaned_data["fees_structure"]
                    joining_date = add_member_form.cleaned_data["joining_date"]

                    if fees_structure:
                        fees_structure = FeesStructure.objects.filter(id=fees_structure).first()

                    # to use the default value of photo which is no-img
                    if photo:
                        member = GymMember(first_name=first_name, last_name=last_name, gender=gender,
                                           date_of_birth=date_of_birth, phone=phone, photo=photo,
                                           leaving_date=datetime.datetime.now(), gym=gym, height=height,
                                           weight=weight, biceps_right=biceps_right, biceps_left=biceps_left,
                                           triceps_right=triceps_right, triceps_left=triceps_left,
                                           fees_structure=fees_structure, joining_date=joining_date)
                    else:
                        member = GymMember(first_name=first_name, last_name=last_name, gender=gender,
                                           date_of_birth=date_of_birth, phone=phone,
                                           leaving_date=datetime.datetime.now(), gym=gym, height=height,
                                           weight=weight, biceps_right=biceps_right, biceps_left=biceps_left,
                                           triceps_right=triceps_right, triceps_left=triceps_left,
                                           fees_structure=fees_structure, joining_date=joining_date)

                    member.save()

                    return redirect('/')
                except Exception, e:
                    return render(request, "add_gym_member.html", {"add_member_form": add_member_form})
            else:
                return render(request, "add_gym_member.html", {"add_member_form": add_member_form})
        return redirect('/accounts/login')


class UpdateGymMember(View):
    def get(self, request, _id, *args, **kwargs):
        if request.user.is_authenticated():
            gym_member = GymMember.objects.filter(id=_id).first()
            initial = {
                'first_name': gym_member.first_name,
                'last_name': gym_member.last_name,
                'gender': gym_member.gender,
                'date_of_birth': gym_member.date_of_birth.date(),
                'phone': gym_member.phone,
                'joining_date': gym_member.joining_date,
                'leaving_date': gym_member.leaving_date,
                'height': gym_member.height,
                'weight': gym_member.weight,
                'biceps_right': gym_member.biceps_right,
                'biceps_left': gym_member.biceps_left,
                'triceps_right': gym_member.triceps_right,
                'triceps_left': gym_member.triceps_left,
                'fees_structure': gym_member.fees_structure,
                'joining_date': gym_member.joining_date.date(),


            }

            # get the gym of gym owner
            gym = Gym.objects.filter(gym_owner_id=request.user.id).first()

            add_member_form = forms.AddGymMemberForm(gym, initial=initial)

            return render(request, "edit_gym_member.html", {"add_member_form": add_member_form, "member_id": _id})
        return redirect('/accounts/login')

    def post(self, request, _id, *args, **kwargs):
        if request.user.is_authenticated():
            # get the gym of gym owner
            gym = Gym.objects.filter(gym_owner_id=request.user.id).first()

            gym_member = GymMember.objects.filter(id=_id).first()

            add_member_form = forms.AddGymMemberForm(gym, request.POST, request.FILES)

            if add_member_form.is_valid():
                try:
                    first_name = add_member_form.cleaned_data["first_name"]
                    last_name = add_member_form.cleaned_data["last_name"]
                    gender = add_member_form.cleaned_data["gender"]
                    date_of_birth = add_member_form.cleaned_data["date_of_birth"]
                    phone = add_member_form.cleaned_data["phone"]
                    photo = add_member_form.cleaned_data["photo"]
                    height = add_member_form.cleaned_data["height"]
                    weight = add_member_form.cleaned_data["weight"]
                    biceps_right = add_member_form.cleaned_data["biceps_right"]
                    biceps_left = add_member_form.cleaned_data["biceps_left"]
                    triceps_right = add_member_form.cleaned_data["triceps_right"]
                    triceps_left = add_member_form.cleaned_data["triceps_left"]
                    joining_date = add_member_form.cleaned_data["joining_date"]
                    fees_structure = add_member_form.cleaned_data["fees_structure"]

                    if fees_structure:
                        fees_structure = FeesStructure.objects.filter(id=fees_structure).first()

                    gym_member.first_name = first_name
                    gym_member.last_name = last_name
                    gym_member.gender = gender
                    gym_member.date_of_birth = date_of_birth
                    gym_member.phone = phone
                    gym_member.height = height
                    gym_member.weight = weight
                    gym_member.biceps_right = biceps_right
                    gym_member.biceps_left = biceps_left
                    gym_member.triceps_right = triceps_right
                    gym_member.triceps_left = triceps_left
                    gym_member.fees_structure = fees_structure
                    gym_member.joining_date = joining_date

                    # to use the default value of photo which is no-img
                    if photo:
                        gym_member.photo = photo

                    gym_member.save()

                    return redirect('/')
                except Exception, e:
                    return render(request, "edit_gym_member.html", {"add_member_form": add_member_form, "member_id": _id})
            else:
                return render(request, "edit_gym_member.html", {"add_member_form": add_member_form, "member_id": _id})

        return redirect('/accounts/login')


@login_required()
def set_fees_structure(request):
    try:
        fees_amount = request.POST['fees_amount']
        fees_structure_type = request.POST['fees_structure_type']
        gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
        fees_structure = FeesStructure.objects.filter(gym=gym, fees_structure_type=fees_structure_type).first()
        if fees_structure:
            fees_structure.fees_amount = fees_amount
            fees_structure.save()
        else:
            FeesStructure.objects.create(gym=gym, fees_amount=fees_amount, fees_structure_type=fees_structure_type)
    except Exception, e:
        print (e.message)
    return redirect('/')


@login_required()
def remove_member(request):
    try:
        member_id = request.POST['member_id']
        gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
        gym_member = GymMember.objects.filter(id=member_id).first()

        if gym_member.gym == gym:
            gym_member.delete()
        else:
            return redirect('/')
    except Exception, e:
        print (e.message)

    return redirect('/')


@login_required()
def list_gym_members(request):
    try:
        gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
        gym_members = GymMember.objects.filter(gym=gym).all()
        return render(request, 'list_gym_members.html', {"gym_members": gym_members})
    except Exception, e:
        print (e.message)
    return redirect('/')


@login_required()
def pay_fees(request):
    try:
        member_id = request.POST['pay_fees_member_id']
        # month = request.POST['pay_fees_month_id']
        # year = request.POST['pay_fees_year_id']
        amount = request.POST['pay_fees_amount']

        gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
        member = GymMember.objects.filter(id=member_id).first()

        last_payment_history = FeesPaymentHistory.objects.filter(gym_member_id=member_id).order_by('-fees_for_year',
                                                                                        '-fees_for_month').first()

        if last_payment_history:
            last_fees_month = last_payment_history.fees_for_month
            last_fees_year = last_payment_history.fees_for_year
        else:
            last_fees_month = member.joining_date.month
            last_fees_year = member.joining_date.year

        if member.fees_structure.fees_structure_type == "Monthly":
            number_of_month = 1
        elif member.fees_structure.fees_structure_type == "Quarterly":
            number_of_month = 3
        elif member.fees_structure.fees_structure_type == "Half-Yearly":
            number_of_month = 6

        next_fees_month = last_fees_month + 1
        next_fees_year = last_fees_year

        for i in range(number_of_month):
            if next_fees_month == 13:
                next_fees_month = 1
                next_fees_year += 1

            FeesPaymentHistory.objects.create(payment_type="offline", amount=amount, discount=0,
                                              fees_for_month=next_fees_month,
                                              fees_for_year=next_fees_year, gym=gym, gym_member=member)

            next_fees_month += 1

    except Exception, e:
        print (e.message)

    return redirect('/')


@login_required()
def check_fees_status(request):
    year = str(datetime.datetime.now().year)

    if 'year' in request.GET.keys():
        year = request.GET['year']

    gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
    gym_members = GymMember.objects.filter(gym=gym).all()
    data = []
    for gym_member in gym_members:
        fees_payments_history = gym_member.feespaymenthistory_set.filter(fees_for_year=year).all().order_by('fees_for_month')
        month_wise_payment_status = []

        leaving_date = gym_member.leaving_date
        if gym_member.joining_date == gym_member.leaving_date:
            leaving_date = None

        for month in range(1, 13):
            first_date_of_month = datetime.datetime.strptime('01' + str(month) + year, "%d%m%Y").replace(tzinfo=pytz.UTC)
            if leaving_date:
                if gym_member.joining_date <= first_date_of_month <= leaving_date:
                    month_wise_payment_status.append("UNPAID")
                else:
                    month_wise_payment_status.append("NA")  # he dint joined the gym until now, or left so NA
            else :  # there is nt leaving date present so from the day of joining mark all  months unpaid until current
                if gym_member.joining_date <= first_date_of_month <= datetime.datetime.today():
                    month_wise_payment_status.append("UNPAID")
                else:
                    month_wise_payment_status.append("NA")  # since this month is of future will mark it NA

        for fees_payment_history in fees_payments_history:
            month_wise_payment_status[fees_payment_history.fees_for_month - 1] = "PAID"

        data.append([gym_member.first_name + " " + gym_member.last_name, month_wise_payment_status])

    return render(request, 'check_fees_status.html', {"data": data, "year": str(year)})


@login_required()
def get_member_details(request, member_id):
    try:
        member = GymMember.objects.filter(id=member_id).first()
        return render(request, 'member_details.html', {"member": member})
    except Exception, e:
        return redirect('/')


@login_required()
def mark_daily_attendance(request):
    try:
        gym = Gym.objects.filter(gym_owner_id=request.user.id).first()
        gym_members = GymMember.objects.filter(gym=gym).all()
        return render(request, 'mark_daily_attendance.html', {"gym_members": gym_members})
    except Exception, e:
        return redirect('/')


MONTHS = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']


@login_required()
def get_member_details_ajax_call(request):
    try:
        member_id = request.GET['member_id']
        member = GymMember.objects.filter(id=member_id).first()

        last_payment_history = FeesPaymentHistory.objects.filter(gym_member_id=member_id).order_by('-fees_for_year', '-fees_for_month').first()

        fees_for_months = ""

        if last_payment_history:
            last_fees_month = last_payment_history.fees_for_month
            last_fees_year = last_payment_history.fees_for_year
        else:
            last_fees_month = member.joining_date.month
            last_fees_year = member.joining_date.year

        if member.fees_structure.fees_structure_type == "Monthly":
            number_of_month = 1
        elif member.fees_structure.fees_structure_type == "Quarterly":
            number_of_month = 3
        elif member.fees_structure.fees_structure_type == "Half-Yearly":
            number_of_month = 6

        next_fees_month = last_fees_month + 1
        next_fees_year = last_fees_year

        for i in range(number_of_month):
            if next_fees_month == 13:
                next_fees_month = 1
                next_fees_year += 1

            fees_for_months += MONTHS[next_fees_month - 1] + "-" + str(next_fees_year) + "  "
            next_fees_month += 1

        return JsonResponse({"status": True, "data": {"fees_Structure": str(member.fees_structure.fees_structure_type),
                                                      "fees_amount": str(member.fees_structure.fees_amount),
                                                      "fees_for_months": fees_for_months}})
    except Exception, e:
        return JsonResponse({"status": False, "data": {"fees_Structure": "None"}})


def generate_csv(request):
    from django.http import HttpResponse
    import csv
    response = HttpResponse(content_type="text/csv")

    writer = csv.writer(response)
    writer.writerow(['First Name, Last Name, Date of Birth'])
    writer.writerow(['Udit', 'Porov', '09/07/1992'])
    writer.writerow(['Sagar', 'Porov', '21/11/1989'])

    return response


def generate_pdf(request):
    from django.http import HttpResponse
    from reportlab.pdfgen import canvas

    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename = "somefilename.pdf"'

    canvas = canvas.Canvas(response)
    canvas.drawString(300, 800, "Hello World!")
    canvas.showPage()
    canvas.save()

    return response
