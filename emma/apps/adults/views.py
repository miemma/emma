#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.views.generic import View
from django.conf import settings

from emma.apps.adults.forms import AdultInfo, AdultPreferences, \
    MedicalInformationBasic, MedicalInformationContacts, MedicalInformationPDA, \
    MedicalInformationInsurance, MedicalInformationSS, MedicalInformationDoctor, \
    MedicaInformationDiseases, AdultHobbieAdd
from emma.core.mixins import ClientRequiredMixin, GetAdultMixin
from emma.core.utils import send_email


class AdultInformation(GetAdultMixin, ClientRequiredMixin, View):
    template_name = 'adults/adult_detail.html'

    def get(self, request, id, **kwargs):
        adultform = self.get_initial_adult_form(
            request, self.get_adult(request)
        )
        preferenceform = self.get_initial_preferences_form(
            request, self.get_adult(request)
        )
        hobbieform = AdultHobbieAdd()
        ctx = {
            'adultform': adultform,
            'preferenceform': preferenceform,
            'hobbieform':hobbieform,
            'adult': self.get_adult(request)
        }
        if self.get_adult(request).medical_information:
            medicalbasicform = self.get_initial_medical_basic_form(
                request, self.get_adult(request)
            )
            medicalcontactsform = self.get_initial_medical_contacts_form(
                request, self.get_adult(request)
            )
            medicalpdaform = self.get_initial_medical_pda_form(
                request, self.get_adult(request)
            )
            medicalinsuranceform = self.get_initial_medical_insurance_form(
                request, self.get_adult(request)
            )
            medicalssform = self.get_initial_medical_ss_form(
                request, self.get_adult(request)
            )
            medicaldoctorform = self.get_initial_medical_doctor_form(
                request, self.get_adult(request)
            )
            medicaldiseasesform = self.get_initial_medical_diseases_form(
                request, self.get_adult(request)
            )
            ctx.update({
                'medicalbasicform': medicalbasicform,
                'medicalcontactsform': medicalcontactsform,
                'medicalpdaform': medicalpdaform,
                'medicalinsuranceform': medicalinsuranceform,
                'medicalssform': medicalssform,
                'medicaldoctorform': medicaldoctorform,
                'medicaldiseasesform': medicaldiseasesform,
            })
        return TemplateResponse(request, self.template_name, ctx)

    def post(self, request, id, **kwargs):
        kwargs = {'request': request, 'adult_id': id}
        if 'medicalbasic_form' in request.POST:
            medicalbasicform = MedicalInformationBasic(request.POST, **kwargs)

            if medicalbasicform.is_valid():
                medicalbasicform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult_med.txt',
                    body='email/notification_edit_adult_med.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información médica actualizada')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': medicalbasicform,
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        elif 'hobbie_form' in request.POST:
            hobbieform = AdultHobbieAdd(request.POST, **kwargs)
            if hobbieform.is_valid():
                hobbieform.save()
                messages.info(self.request, 'Hobbie añadido')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': hobbieform,
                }
                return render(request, self.template_name, ctx)

        elif 'medicalcontacts_form' in request.POST:
            medicalcontactsform = MedicalInformationContacts(request.POST, **kwargs)

            if medicalcontactsform.is_valid():
                medicalcontactsform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult_med.txt',
                    body='email/notification_edit_adult_med.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información médica actualizada')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': medicalcontactsform,
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        elif 'medicalpda_form' in request.POST:
            medicalpdaform = MedicalInformationPDA(request.POST, **kwargs)

            if medicalpdaform.is_valid():
                medicalpdaform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult_med.txt',
                    body='email/notification_edit_adult_med.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información médica actualizada')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': medicalpdaform,
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        elif 'medicalinsurance_form' in request.POST:
            medicalinsuranceform = MedicalInformationInsurance(request.POST, **kwargs)

            if medicalinsuranceform.is_valid():
                medicalinsuranceform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult_med.txt',
                    body='email/notification_edit_adult_med.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información médica actualizada')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': medicalinsuranceform,
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        elif 'medicalss_form' in request.POST:
            medicalssform = MedicalInformationSS(request.POST, **kwargs)

            if medicalssform.is_valid():
                medicalssform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult_med.txt',
                    body='email/notification_edit_adult_med.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información médica actualizada')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': medicalssform,
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        elif 'medicaldoctor_form' in request.POST:
            medicaldoctorform = MedicalInformationDoctor(request.POST, **kwargs)

            if medicaldoctorform.is_valid():
                medicaldoctorform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult_med.txt',
                    body='email/notification_edit_adult_med.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información médica actualizada')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': medicaldoctorform,
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        elif 'medicaldiseases_form' in request.POST:
            medicaldiseasesform = MedicaInformationDiseases(request.POST, **kwargs)

            if medicaldiseasesform.is_valid():
                medicaldiseasesform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult_med.txt',
                    body='email/notification_edit_adult_med.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información médica actualizada')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': medicaldiseasesform,
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        elif 'adult_form' in request.POST:

            adultform = AdultInfo(request.POST, request.FILES, **kwargs)

            if adultform.is_valid():
                adultform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult.txt',
                    body='email/notification_edit_adult.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': 'dadas',
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información del adulto actualizda')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': adultform,
                    'preferenceform': self.get_initial_preferences_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd(),
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                }
                return render(request, self.template_name, ctx)

        elif 'preference_form' in request.POST:

            preferenceform = AdultPreferences(request.POST, **kwargs)
            if preferenceform.is_valid():
                preferenceform.save()
                send_email(
                    subject='email/subjects/notification_edit_adult.txt',
                    body='email/notification_edit_adult.html',
                    context={
                        'user_full_name': request.user.get_full_name,
                        'adult_full_name': self.get_adult(request).first_name,
                    },
                    to_email=[settings.DEFAULT_EMAIL_TO],
                )
                messages.info(self.request, 'Información del adulto actualizda')
                return redirect(reverse_lazy('adults:dashboard_adult',
                                             kwargs={'id': id}))
            else:
                ctx = {
                    'adultform': self.get_initial_adult_form(
                        request, self.get_adult(request)
                    ),
                    'preferenceform': preferenceform,
                    'medicalbasicform': self.get_initial_medical_basic_form(
                        request, self.get_adult(request)
                    ),
                    'medicalcontactsform': self.get_initial_medical_contacts_form(
                        request, self.get_adult(request)
                    ),
                    'medicalpdaform': self.get_initial_medical_pda_form(
                        request, self.get_adult(request)
                    ),
                    'medicalinsuranceform': self.get_initial_medical_insurance_form(
                        request, self.get_adult(request)
                    ),
                    'medicalssform': self.get_initial_medical_ss_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldoctorform': self.get_initial_medical_doctor_form(
                        request, self.get_adult(request)
                    ),
                    'medicaldiseasesform': self.get_initial_medical_diseases_form(
                        request, self.get_adult(request)
                    ),
                    'adult': self.get_adult(request),
                    'hobbieform': AdultHobbieAdd()
                }
                return render(request, self.template_name, ctx)

        else:
            raise Http404("No se encontró la pagina")

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
            }
        )
        return form

    @staticmethod
    def get_initial_medical_basic_form(request, adult):
        form = MedicalInformationBasic(
            initial={
                'blood_type':
                    adult.medical_information.blood_type,
            }
        )
        return form

    @staticmethod
    def get_initial_medical_contacts_form(request, adult):
        form = MedicalInformationContacts(
            initial={
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
            }
        )
        return form

    @staticmethod
    def get_initial_medical_pda_form(request, adult):
        form = MedicalInformationPDA(
            initial={
                'knows_pda':
                    adult.medical_information.knows_pda,
                'exercise_pda':
                    adult.medical_information.exercise_pda,
            }
        )
        return form

    @staticmethod
    def get_initial_medical_insurance_form(request, adult):
        form = MedicalInformationInsurance(
            initial={
                'has_medical_insurance':
                    adult.medical_information.has_medical_insurance,
                'insurance_company':
                    adult.medical_information.insurance_company,
                'policy_number':
                    adult.medical_information.policy_number,
                'policy_expiration_date':
                    adult.medical_information.policy_expiration_date,
            }
        )
        return form

    @staticmethod
    def get_initial_medical_ss_form(request, adult):
        form = MedicalInformationSS(
            initial={
                'has_social_security':
                    adult.medical_information.has_social_security,
                'social_security_number':
                    adult.medical_information.social_security_number,
            }
        )
        return form

    @staticmethod
    def get_initial_medical_doctor_form(request, adult):
        form = MedicalInformationDoctor(
            initial={
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
            }
        )
        return form

    @staticmethod
    def get_initial_medical_diseases_form(request, adult):
        form = MedicaInformationDiseases(
            initial={
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

    @staticmethod
    def get_initial_preferences_form(request, adult):
        form = AdultPreferences(
            initial={
                'familiar_structure': adult.familiar_structure,
                'personality': adult.personality,
            }
        )
        return form