#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.views.generic import View

from emma.apps.adults.forms import AdultInfo, MedicalInfo
from emma.core.mixins import ClientRequiredMixin, GetAdultMixin


class AdultInformation(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'adults/adult_detail.html'

    def get(self, request, id, **kwargs):
        adultform = self.get_initial_adult_form(
            request, self.get_adult(request)
        )
        medicalform = self.get_initial_medical_form(
            request, self.get_adult(request)
        )
        ctx = {
            'adultform': adultform,
            'medicalform': medicalform,
            'adult': self.get_adult(request)
        }
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request, id, **kwargs):
        kwargs = {'request': request, 'adult_id': id}

        if 'medical_form' in request.POST:
            medicalform = MedicalInfo(request.POST, **kwargs)

            if medicalform.is_valid():
                medicalform.save()
                messages.info(self.request, 'Medical information update')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {'medicalform': medicalform}
                return render(request, self.template_name, ctx)
        elif 'adult_form' in request.POST:

            adultform = AdultInfo(request.POST, request.FILES, **kwargs)

            if adultform.is_valid():
                adultform.save()
                messages.info(self.request, 'User update')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {'adultform': adultform}
                return render(request, self.template_name, ctx)
        else:
            raise Http404("No se encontro la pagina")

    @staticmethod
    def get_initial_adult_form(request, adult):
        form = AdultInfo(
            initial={
                'first_name': adult.first_name,
                'last_name': adult.last_name,
                'birthday': adult.birthday,
                'street': adult.address.street,
                'num_ext': adult.address.outdoor_number,
                'num_int': adult.address.interior_number,
                'delegation': adult.address.municipality,
                'colony': adult.address.colony,
                'postal_code': adult.address.postal_code,
                'reference': adult.address.reference,
                'photo': adult.photo,
                'personality': adult.personality,
                'familiar_structure': adult.familiar_structure,
                'description': adult.description,
            }
        )
        return form

    @staticmethod
    def get_initial_medical_form(request, adult):
        print (adult.medical_information)
        form = MedicalInfo(
            initial={
                'blood_type':
                    adult.medical_information.blood_type,
                'emergency_contact_1_full_name':
                    adult.medical_information.emergency_contact_1.full_name,
                'emergency_contact_1_relation':
                    adult.medical_information.emergency_contact_1.relation,
                'emergency_contact_1_cell_phone':
                    adult.medical_information.emergency_contact_1.cell_phone,
                'emergency_contact_1_home_phone':
                    adult.medical_information.emergency_contact_1.home_phone,
                'emergency_contact_2_full_name':
                    adult.medical_information.emergency_contact_2.full_name,
                'emergency_contact_2_relation':
                    adult.medical_information.emergency_contact_2.relation,
                'emergency_contact_2_cell_phone':
                    adult.medical_information.emergency_contact_2.cell_phone,
                'emergency_contact_2_home_phone':
                    adult.medical_information.emergency_contact_2.home_phone,
                'knows_pda':
                    adult.medical_information.knows_pda,
                'exercise_pda':
                    adult.medical_information.exercise_pda,
                'has_medical_insurance':
                    adult.medical_information.has_medical_insurance,
                'insurance_company':
                    adult.medical_information.insurance_company,
                'policy_number':
                    adult.medical_information.policy_number,
                'policy_expiration_date':
                    adult.medical_information.policy_expiration_date,
                'has_social_security':
                    adult.medical_information.has_social_security,
                'social_security_number':
                    adult.medical_information.social_security_number,
                'doctor_first_name':
                    adult.medical_information.doctor.first_name,
                'doctor_last_name':
                    adult.medical_information.doctor.last_name,
                'doctor_cell_phone':
                    adult.medical_information.doctor.cell_phone,
                'doctor_home_phone':
                    adult.medical_information.doctor.home_phone,
                'doctor_working_institution':
                    adult.medical_information.doctor.working_institution,
                'doctor_professional_id':
                    adult.medical_information.doctor.professional_id,
                'diseases':
                    adult.medical_information.diseases,
                'current_medications':
                    adult.medical_information.current_medications,
                'drug_allergy':
                    adult.medical_information.drug_allergy,
                'food_allergy':
                    adult.medical_information.food_allergy,
            }
        )
        return form
