from email import message
from email.message import Message
from django.shortcuts import render
from .models import Member
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import boto3

# Create your views here.


@login_required
def register(request):
    if request.method == 'POST':
        member_gfx = request.POST['gfxNumber']
        region = request.POST['region']
        district = request.POST['district']
        society = request.POST['society']
        title = request.POST['title']
        first_name = request.POST['firstName']
        middle_name = request.POST['middleName']
        last_name = request.POST['lastName']
        preferred_name = request.POST['prefName']
        gender = request.POST['gender']
        date_of_birth = request.POST['date']
        address = request.POST['address']
        telephone = request.POST['tel']
        educational_level = request.POST['education']
        hometown = request.POST['hometown']
        id_type = request.POST['id']
        id_number = request.POST['idNumber']
        marriage_status = request.POST['marriage']
        spoue_name = request.POST['spouseName']
        spouse_occupation = request.POST['spouseOccupation']
        spouse_number = request.POST['spouseNumber']
        next_of_kin = request.POST['kinName']
        number_kin = request.POST['NumPartners']
        relationship_kin = request.POST['kinRelation']
        number_kin = request.POST['kinNumber']
        Num_partners = request.POST['NumPartners']
        family_size = request.POST['familySize']
        image = request.FILES['profile']
        owner_of_farm = request.POST['farmOwner']
        number_of_labourers = request.POST['nlabourers']
        duration = request.POST['duration']
        name_of_owner = request.POST['ownerName']
        owners_gfx = request.POST['ownerGFX']
        how_many_people = request.POST['numPeople']
        names_of_families = request.POST['familyPeople[]']
        crop_cultivated = request.POST['cropcultivated']
        farm_size = request.POST['farmSize']
        farm_location = request.POST['farmLocation']
        years_in_farming = request.POST['yearFarming']
        side_business = request.POST['sideBusiness']
        side_business_specify = request.POST['sideBuss']
        current_side_business = request.POST['currentBuss']
        current_business_specify = request.POST['sideBuzz']
        average_yield = request.POST['averageYield']
        previous_yield = request.POST['PrevYield']
        benefit_from_farm = request.POST['farmBenefit']
        buyer_of_produce = request.POST['buyer']
        number_of_times = request.POST['howOften']
        benefit_from_buyer = request.POST['buyerBenefits']
        usage_of_funds = request.POST['usageoffunds']
        bank_transacting_with = request.POST['questionBanks']
        other_specify = request.POST['bankT']
        how_long = request.POST['durat']
        interes_in_gnacofa = request.POST['interest']
        specify_why = request.POST['specif']

        member = Member.objects.filter(member_gfx = member_gfx)
        if member:
            messages.error(
            request, f'This Member [{member_gfx}] has already been entered')
        elif first_name =='' or region == '' or district == '' or society  == '':
            if first_name:
                messages.error(request, f"first name is required")
            elif region:
                messages.error(request, f"Region is required")
            elif district:
                messages.error(request, f"district name is required")
            else:
                messages.error(request, f"society is required")
           
        else:
            new_member = Member(member_gfx=member_gfx, region=region, district=district, society=society, title=title, first_name=first_name, middle_name=middle_name, last_name=last_name, preferred_name=preferred_name, gender=gender, date_of_birth=date_of_birth, address=address, telephone=telephone, educational_level=educational_level, hometown=hometown, id_type=id_type, id_number=id_number, marriage_status=marriage_status, spoue_name=spoue_name, spouse_occupation=spouse_occupation, spouse_number=spouse_number, next_of_kin=next_of_kin, relationship_kin=relationship_kin, number_kin=number_kin, Num_partners=Num_partners, family_size=family_size, image=image, owner_of_farm=owner_of_farm, number_of_labourers=number_of_labourers, duration=duration, name_of_owner=name_of_owner,
            owners_gfx=owners_gfx, how_many_people=how_many_people, names_of_families=names_of_families, crop_cultivated=crop_cultivated, farm_size=farm_size, farm_location=farm_location, years_in_farming=years_in_farming, side_business=side_business, side_business_specify=side_business_specify, current_side_business=current_side_business, current_business_specify=current_business_specify, average_yield=average_yield, previous_yield=previous_yield, benefit_from_farm=benefit_from_farm, buyer_of_produce=buyer_of_produce, number_of_times=number_of_times, benefit_from_buyer=benefit_from_buyer, usage_of_funds=usage_of_funds, bank_transacting_with=bank_transacting_with, other_specify=other_specify, how_long=how_long, interes_in_gnacofa=interes_in_gnacofa, specify_why=specify_why)

            messages.success(
                request, f'Accout Created successfully for [{member_gfx}]')
            new_member.save()
    return render(request, 'members/mregister.html')