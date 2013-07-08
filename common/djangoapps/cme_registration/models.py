from django.db import models
from student.models import UserProfile

# Create your models here.

    
#Fields for CME specific registration page
class CmeUserProfile(UserProfile):
    class Meta:
        db_table = "cme_registration"
        
    PROFESSION_CHOICES = (('Allied Health Professional', 'Allied Health Professional'),
                          ('Fellow', 'Fellow'),
                          ('Nurse', 'Nurse'),
                          ('Nurse Practioner', 'Nurse Practioner'),
                          ('Physician', 'Physician'),
                          ('Physician Assistant', 'Physician Assistant'),
                          ('Resident', 'Resident'),
                          ('Student', 'Student'))
    profession = models.CharField(
                                  blank=True, null=True, max_length=30, choices=PROFESSION_CHOICES
                                  )
 
    PROFESSIONAL_DESIGNATION_CHOICES = (('MD', 'MD'),
                                        ('DO', 'DO'),
                                        ('PA', 'PA'),
                                        ('NP', 'NP'),
                                        ('RN', 'RN'))
    professional_designation = models.CharField(
                                                blank=True, null=True, max_length=3, choices=PROFESSIONAL_DESIGNATION_CHOICES
                                                )
    license_number = models.CharField(
                                      blank=True, null=True, max_length=255
                                      )
    organization = models.CharField(
                                      blank=True, null=True, max_length=255
                                      )
    stanford_affiliated = models.BooleanField(default=0)
    HOW_STANFORD_AFFILIATED_CHOICES = (('Lucile Packard Children\'s Hospital at Stanford', 'Lucile Packard Children\'s Hospital at Stanford'),
                                       ('Packard Children\'s Health Alliance (PCHA)', 'Packard Children\'s Health Alliance (PCHA)'),
                                       ('Stanford Hospital & Clinics', 'Stanford Hospital & Clinics'),
                                       ('Stanford University', 'Stanford University'),
                                       (' University Healthcare Alliance (UHA)', ' University Healthcare Alliance (UHA)'),
                                       (' Other, please enter:', ' Other, please enter:'))
    how_stanford_affiliated = models.CharField(
                                               blank=True, null=True, max_length=50, choices=HOW_STANFORD_AFFILIATED_CHOICES)
    PATIENT_POPULATION_CHOICES = (('Adult', 'Adult'),
                                  ('Pediatric', 'Pediatric'),
                                  ('Both (Adult/Pediatric)', 'Both (Adult/Pediatric)'))
    patient_population = models.CharField(
                                          blank=True, null=True, max_length=25, choices=PATIENT_POPULATION_CHOICES)
    specialty = models.CharField(
                                 blank=True, null=True, max_length=50)
    sub_specialty = models.CharField(
                                     blank=True, null=True, max_length=50)
    address_1 = models.TextField(blank=True, null=True)
    address_2 = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    STATE_CHOICES = (('Alabama', 'Alabama'),
                     ('Alaska', 'Alaska'),
                     ('Arizona', 'Arizona'),
                     ('Arkansas', 'Arkansas'),
                     ('California', 'California'),
                     ('Colorado', 'Colorado'),
                     ('Connecticut', 'Connecticut'),
                     ('Delaware', 'Deleware'),
                     ('District of Columbia', 'District of Columbia'),
                     ('Florida', 'Florida'),
                     ('Georgia', 'Georgia'),
                     ('Hawaii', 'Hawaii'),
                     ('Idaho', 'Idaho'),
                     ('Illinois', 'Indiana'),
                     ('Iowa', 'Iowa'),
                     ('Kansas', 'Kansas'),
                     ('Kentucky', 'Kentucky'),
                     ('Louisiana', 'Louisiana'),
                     ('Maine', 'Maine'),
                     ('Maryland', 'Maryland'),
                     ('Massachusetts', 'Massachusetts'),
                     ('Michigan', 'Michigan'),
                     ('Minnesota', 'Minnesota'),
                     ('Mississippi', 'Mississippi'),
                     ('Missouri', 'Missouri'),
                     ('Montana', 'Montana'),
                     ('Nebraska', 'Nebraska'),
                     ('Nevada', 'Nevada'),
                     ('Vermont', 'Vermont'),
                     ('Virginia', 'Virginia'),
                     ('Washington', 'Washington'),
                     ('West Virginia', 'West Virginia'),
                     ('Wisconsin', 'Wisconsin'),
                     ('Wyoming', 'Wyoming'),
                     ('American Samoa', 'American Samoa'),
                     ('Armed Forces America', 'Armed Forces America'),
                     ('Armed Forces Europe', 'Armed Forces Europe'),
                     ('Armed Forces Pacific', 'Armed Forces Pacific'),
                     ('Guam', 'Guam'),
                     ('Northern Mariana Islands', 'Northern, Mariana Islands'),
                     ('Palau', 'Palau'),
                     ('Puerto Rico', 'Puerto Rico'),
                     ('Utah', 'Utah'),
                     ('Virgin Island', 'Virgin Island'),
                     ('Other', 'Other'),
                     ('Alberta', 'Alberta'),
                     ('British Columbia', 'British Columbia'),
                     ('Manitoba', 'Manitoba'),
                     ('Nanavut', 'Nanavut'),
                     ('New Brunswick', 'New Brunswick'),
                     ('Newfoundland and Labrador', 'Newfoundland and Labrador'),
                     ('Northwest Territories', 'Northwest Territories'),
                     ('Nova Scotia', 'Nova Scotia'),
                     ('Ontario', 'Ontario'),
                     ('Prince Edward Island', 'Prince Edward Island'),
                     ('Quebec', 'Quebec'),
                     ('Saskatchewan', 'Saskatchewan'),
                     ('Yukon Territory', 'Yukon Territory'))
 
    state_province = models.CharField(
                                      blank=True, null=True, max_length=50, choices=STATE_CHOICES)
    postal_code = models.CharField(blank=True, null=True, max_length=20)
    COUNTRY_CHOICES = (('United States', 'United States'),
                       ('Afghanistan', 'Afghanistan'),
                       ('Aland Islands', 'Aland Islands'),
                       ('Albania', 'Albania'),
                       ('Algeria', 'Algeria'),
                       ('American Samoa', 'American Samoa'),
                       ('Andorra', 'Andorra'),
                       ('Angola', 'Angola'),
                       ('Anguilla', 'Anguilla'),
                       ('Antarctica', 'Antarctica'),
                       ('Antigua And Barbuda', 'Antigua And Barbuda'),
                       ('Argentina', 'Argentina'),
                       ('Armenia', 'Armenia'),
                       ('Aruba', 'Aruba'),
                       ('Australia', 'Australia'),
                       ('Austria', 'Austria'),
                       ('Azerbaijan', 'Azerbaijan'),
                       ('Bahamas', 'Bahamas'),
                       ('Bahrain', 'Bahrain'),
                       ('Bangladesh', 'Bangladesh'),
                       ('Barbados', 'Barbados'),
                       ('Belarus', 'Belarus'),
                       ('Belgium', 'Belgium'),
                       ('Belize', 'Belize'),
                       ('Benin', 'Benin'),
                       ('Bermuda', 'Bermuda'),
                       ('Bhutan', 'Bhutan'),
                       ('Bolivia', 'Bolivia'),
                       ('Bosnia And Herzegovina', 'Bosnia And Herzegovina'),
                       ('Botswana', 'Botswana'),
                       ('Bouvet Island', 'Bouvet Island'),
                       ('Brazil', 'Brazil'),
                       ('British Indian Ocean Territory', 'British Indian Ocean Territory'),
                       ('Brunei Darussalam', 'Brunei Darussalam'),
                       ('Bulgaria', 'Bulgaria'),
                       ('Burkina Faso', 'Burkina Faso'),
                       ('Burundi', 'Burundi'),
                       ('Cambodia', 'Cambodia'),
                       ('Cameroon', 'Cameroon'),
                       ('Canada', 'Canada'),
                       ('Cape Verde', 'Cape Verde'),
                       ('Cayman Islands', 'Cayman Islands'),
                       ('Central African Republic', 'Central African Republic'),
                       ('Chad', 'Chad'),
                       ('Chile', 'Chile'),
                       ('China', 'China'),
                       ('Christmas Island', 'Christmas Island'),
                       ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
                       ('Colombia', 'Colombia'),
                       ('Comoros', 'Comoros'),
                       ('Congo', 'Congo'),
                       ('Congo, The Democratic Republic OfThe', 'Congo, The Democratic Republic OfThe'),
                       ('Cook Islands', 'Cook Islands'),
                       ('Costa Rica', 'Costa Rica'),
                       ('Cote D\'lvoire', 'Cote D\'lvoire'),
                       ('Croatia', 'Croatia'),
                       ('Cuba', 'Cuba'),
                       ('Cyprus', 'Cyprus'),
                       ('Czech Republic', 'Czech Republic'),
                       ('Denmark', 'Denmark'),
                       ('Djibouti', 'Djibouti'),
                       ('Dominica', 'Dominica'),
                       ('Dominican Republic', 'Dominican Republic'),
                       ('Ecuador', 'Ecuador'),
                       ('Egypt', 'Egypt'),
                       ('El Salvador', 'El Salvador'),
                       ('Equatorial Guinea', 'Equatorial Guinea'),
                       ('Eritrea', 'Eritrea'),
                       ('Estonia', 'Estonia'),
                       ('Ethiopia', 'Ethiopia'),
                       ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'),
                       ('Faroe Islands', 'Faroe Islands'),
                       ('Fiji', 'Fiji'),
                       ('Finland', 'Finland'),
                       ('France', 'France'),
                       ('French Guiana', 'French Guiana'),
                       ('French Polynesia', 'French Polynesia'),
                       ('French Southern Territories', 'French Southern Territories'),
                       ('Gabon', 'Gabon'),
                       ('Gambia', 'Gambia'),
                       ('Georgia', 'Georgia'),
                       ('Germany', 'Germany'),
                       ('Ghana', 'Ghana'),
                       ('Gibraltar', 'Gibraltar'),
                       ('Greece', 'Greece'),
                       ('Greenland', 'Greenland'),
                       ('Grenada', 'Grenada'),
                       ('Guadeloupe', 'Guadeloupe'),
                       ('Guam', 'Guam'),
                       ('Guatemala', 'Guatemala'),
                       ('Guernsey', 'Guernsey'),
                       ('Guinea', 'Guinea'),
                       ('Guinea-Bissau', 'Guinea-Bissau'),
                       ('Guyana', 'Guyana'),
                       ('Haiti', 'Haiti'),
                       ('Heard Island And McDonald Is lands', 'Heard Island And McDonald Is lands'),
                       ('Holy See (V.atican City State)', 'Holy See (V.atican City State)'),
                       ('Honduras', 'Honduras'),
                       ('Hong Kong', 'Hong Kong'),
                       ('Hungary', 'Hungary'),
                       ('Iceland', 'Iceland'),
                       ('India', 'India'),
                       ('Indonesia', 'Indonesia'),
                       ('Iran, Islamic Republic Of', 'Iran, Islamic Republic Of'),
                       ('Iraq', 'Iraq'),
                       ('Ireland', 'Ireland'),
                       ('Isle Of Man', 'Isle Of Man'),
                       ('Israel', 'Israel'),
                       ('Italy', 'Italy'),
                       ('Jamaica', 'Jamaica'),
                       ('Japan', 'Japan'),
                       ('Jersey', 'Jersey'),
                       ('Jordan', 'Jordan'),
                       ('Kazakhstan', 'Kazakhstan'),
                       ('Kenya', 'Kenya'),
                       ('Kiribati', 'Kiribati'),
                       ('Korea, Democratic People\'s Republic Of', 'Korea, Democratic People\'s Republic Of'),
                       ('Korea, Republic Of', 'Korea, Republic Of'),
                       ('Kuwait', 'Kuwait'),
                       ('Kyrgyzstan', 'Kyrgyzstan'),
                       ('Lao People\'s Democratic Republic', 'Lao People\'s Democratic Republic'),
                       ('Latvia', 'Latvia'),
                       ('Lebanon', 'Lebanon'),
                       ('Lesotho', 'Lesotho'),
                       ('Liberia', 'Liberia'),
                       ('Libyan Arab Jamahiriya', 'Libyan Arab Jamahiriya'),
                       ('Liechtenstein', 'Liechtenstein'),
                       ('Lithuania', 'Lithuania'),
                       ('Luxembourg', 'Luxembourg'),
                       ('MacAo', 'MacAo'),
                       ('MacEdonia, The Former Yugoslav Republic Of', 'MacEdonia, The Former Yugoslav Republic Of'),
                       ('Madagascar', 'Madagascar'),
                       ('Malawi', 'Malawi'),
                       ('Malaysia', 'Malaysia'),
                       ('Maldives', 'Maldives'),
                       ('Mali', 'Mali'),
                       ('Malta', 'Malta'),
                       ('Marshall Islands', 'Marshall Islands'),
                       ('Martinique', 'Martinique'),
                       ('Mauritan ia', 'Mauritan ia'),
                       ('Mauritius', 'Mauritius'),
                       ('Mayotte', 'Mayotte'),
                       ('Mexico', 'Mexico'),
                       ('Micronesia, Federated States Of', 'Micronesia, Federated States Of'),
                       ('Moldova, Republic Of', 'Moldova, Republic Of'),
                       ('Monaco', 'Monaco'),
                       ('Mongolia', 'Mongolia'),
                       ('Montenegro', 'Montenegro'),
                       ('Montserrat', 'Montserrat'),
                       ('Morocco', 'Morocco'),
                       ('Mozambique', 'Mozambique'),
                       ('Myanmar', 'Myanmar'),
                       ('Namibia', 'Namibia'),
                       ('Nauru', 'Nauru'),
                       ('Nepal', 'Nepal'),
                       ('Netherlands', 'Netherlands'),
                       ('Netherlands Antilles', 'Netherlands Antilles'),
                       ('New Caledonia', 'New Caledonia'),
                       ('New Zealand', 'New Zealand'),
                       ('Nicaragua', 'Nicaragua'),
                       ('Niger', 'Niger'),
                       ('Nigeria', 'Nigeria'),
                       ('Niue', 'Niue'),
                       ('Norfolk Island', 'Norfolk Island'),
                       ('Northern Mariana Islands', 'Northern Mariana Islands'),
                       ('Norway', 'Norway'),
                       ('Not Specified', 'Not Specified'),
                       ('Oman', 'Oman'),
                       ('Other', 'Other'),
                       ('Pakistan', 'Pakistan'),
                       ('Palau', 'Palau'),
                       ('Palestinian Territory, Occupied', 'Palestinian Territory, Occupied'),
                       ('Panama', 'Panama'),
                       ('Papua New Guinea', 'Papua New Guinea'),
                       ('Paraguay', 'Paraguay'),
                       ('Peru', 'Peru'),
                       ('Philippines', 'Philippines'),
                       ('Pitc.airn', 'Pitc.airn'),
                       ('Poland', 'Poland'),
                       ('Portugal', 'Portugal'),
                       ('Puerto Rico', 'Puerto Rico'),
                       ('Qatar', 'Qatar'),
                       ('Reunion', 'Reunion'),
                       ('Romania', 'Romania'),
                       ('Russia', 'Russia'),
                       ('Rwanda', 'Rwanda'),
                       ('Saint Helena', 'Saint Helena'),
                       ('Saint Kitts And Nevis', 'Saint Kitts And Nevis'),
                       ('Saint Lucia', 'Saint Lucia'),
                       ('Saint Pierre And Miquelon', 'Saint Pierre And Miquelon'),
                       ('Saint Vincent And The Grenadines', 'Saint Vincent And The Grenadines'),
                       ('Samoa', 'Samoa'),
                       ('San Marino', 'San Marino'),
                       ('Sao Tome And Principe', 'Sao Tome And Principe'),
                       ('Saudi Arabia', 'Saudi Arabia'),
                       ('Senegal', 'Senegal'),
                       ('Serbia', 'Serbia'),
                       ('Seychelles', 'Seychelles'),
                       ('Sierra Leone', 'Sierra Leone'),
                       ('Singapore', 'Singapore'),
                       ('Slovakia', 'Slovakia'),
                       ('Slovenia', 'Slovenia'),
                       ('Solomon Islands', 'Solomon Islands'),
                       ('Somalia', 'Somalia'),
                       ('South Africa', 'South Africa'),
                       ('South Georgia And The South Sandwich Islands', 'South Georgia And The South Sandwich Islands'),
                       ('Spain', 'Spain'),
                       ('Sri Lanka', 'Sri Lanka'),
                       ('Sudan', 'Sudan'),
                       ('Suriname', 'Suriname'),
                       ('Svalbard And Jan Mayen', 'Svalbard And Jan Mayen'),
                       ('Swaziland', 'Swaziland'),
                       ('Sweden', 'Sweden'),
                       ('Switzerland', 'Switzerland'),
                       ('Syrian Alab Republic', 'Syrian Alab Republic'),
                       ('Taiwan', 'Taiwan'),
                       ('Tajikistan', 'Tajikistan'),
                       ('Tanzania, United Republic Of', 'Tanzania, United Republic Of'),
                       ('Thailand', 'Thailand'),
                       ('Timor-Leste', 'Timor-Leste'),
                       ('Togo', 'Togo'),
                       ('Tokelau', 'Tokelau'),
                       ('Tonga', 'Tonga'),
                       ('Trinidad And Tobago', 'Trinidad And Tobago'),
                       ('Tunisia', 'Tunisia'),
                       ('Turkey', 'Turkey'),
                       ('Turkmenistan', 'Turkmenistan'),
                       ('Turks And Caicos Islands', 'Turks And Caicos Islands'),
                       ('Tuvalu', 'Tuvalu'),
                       ('U.S. Minor Outlying Islands', 'U.S. Minor Outlying Islands'),
                       ('Uganda', 'Uganda'),
                       ('Ukraine', 'Ukraine'),
                       ('United Alab Emirates', 'United Alab Emirates'),
                       ('United Kingdom', 'United Kingdom'),
                       ('Uruguay', 'Uruguay'),
                       ('Uzbekistan', 'Uzbekistan'),
                       ('Vanuatu', 'Vanuatu'),
                       ('Venezuela', 'Venezuela'),
                       ('Viet Nam', 'Viet Nam'),
                       ('Virgin Islands, British', 'Virgin Islands, British'),
                       ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'),
                       ('Wallis And Futuna', 'Wallis And Futuna'),
                       ('Western Sahara', 'Western Sahara'),
                       ('Yemen', 'Yemen'),
                       ('Zambia', 'Zambia'),
                       ('Zimbabwe', 'Zimbabwe'))
     
    country = models.CharField(blank=True, null=True, max_length=50, choices=COUNTRY_CHOICES)
    phone_number = models.CharField(blank=True, null=True, max_length=30)
    extension = models.CharField(blank=True, null=True, max_length=10)
    fax = models.CharField(blank=True, null=True, max_length=30)
    HEAR_ABOUT_US_CHOICES = (('Direct Mail Brochure', 'Direct Mail Brochure'),
                             ('Email Announcement', 'Email Announcement'),
                             ('SCCME Web site', 'SCCME Web site'),
                             ('Friend/Colleague', 'Friend/Colleague'),
                             ('Other (free form)', 'Other (free form)'))
    hear_about_us = models.CharField(blank=True, null=True, max_length=25)
    mailing_list = models.BooleanField(default=0)
     