from django.db import models


custstatus = (
    ("Open","Open"),
    ("Contacted","Contacted"),
    ("Qualified","Qualified"),
    ("Unqualified","Unqualified")
)

custsource = (
    ("Networking","Networking"),
    ("Phone Enquiry","Phone Enquiry"),
    ("Cold Call","Cold Call"),
    ("Cold Email","Cold Email"),
    ("Trade Show","Trade Show"),
    ("Employee Referral","Employee Referral"),
    ("Client Referral","Client Referral"),
    ("External Referral","External Referral"),
    ("SEO/SEM Campaign","SEO/SEM Campaign"),
    ("Email Marketing Campaign","Email Marketing Campaign"),
    ("Web-Contact Form","Web-Contact Form"),
    ("Web-Enquiry Form","Web-Enquiry Form"),
    ("Web-Search","Web-Search"),
    ("Webinar","Webinar"),
    ("Other","Other"),
)
custrating = (
    ("Cold","Cold"),
    ("Warm","Warm"),
    ("Hot","Hot"),
)
custleadstage = (
    ("Lead Stage","Lead Stage"),
    ("2","Prospect"),
    ("3","Presentation/Pitch"),
    ("4","Demo"),
    ("5","Planning"),
    ("9","Query Solving"),
    ("10","Request for Proposal"),
    ("11","Negotiation"),
    ("12","LOI/Heads of Terms"),
    ("13","Signed Agreement"),
    ("14","Invoice Raised"),
    ("15","Signed Up"),
    ("16","Add Company"),
    ("17","Add Outlet"),
    ("18","Offers Designed"),
    ("19","Campaign Created"),
    ("20","Plugin Integration"),
    ("21","Campaign Live"),
    ("22","Offers Active"),
    ("23","DNS Integration"),
    ("24","Customer"),
    ("25","Single Offer Created"),
    ("26","Parked Funnel")
)
titlechoice = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Miss', 'Miss'),
    ('Ms.', 'Ms.'),
)
Gender = (
    ("Male","Male"),
    ("Female","Female")
)
Martial_Status = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('Widowed', 'Widowed'),
)
Occupation = (
    ('Employed', 'Employed'),
    ('Self-Employed', 'Self-Employed'),
    ('Student', 'Student'),
    ('Unemployed', 'Unemployed'),
)
TYPE_CHOICES = (
    ("RETAIL", 'Retail'),
        # Add other choices here if needed
)
# Create your models here.

class Details(models.Model):
    phone_code = models.IntegerField()
    children = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    cust_status = models.CharField(max_length=255, choices=custstatus)
    cust_source = models.CharField(max_length=255,choices=custsource)
    cust_rating = models.CharField(max_length=255,choices=custrating)
    cust_lead = models.CharField(max_length=255,choices=custleadstage)
    title = models.CharField(max_length=255,choices=titlechoice)
    cust_first_name = models.CharField(max_length=255)
    cust_last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_no = models.IntegerField()
    phone_no2 = models.IntegerField()
    landline1 = models.IntegerField()
    landline2 = models.IntegerField()
    cust_dob = models.DateField()
    gender = models.CharField(max_length=255,choices = Gender)
    martial_status = models.CharField(max_length=255,choices=Martial_Status)
    no_of_children = models.IntegerField()
    occupation = models.CharField(max_length=255,choices=Occupation)
    sector = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    lead_social_twitter = models.CharField(max_length=255)
    lead_social_fb = models.CharField(max_length=255)
    lead_social_insta = models.CharField(max_length=255)
    lead_social_linkedin = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    area_building = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.IntegerField()
    shipping_address1 = models.CharField(max_length=255)
    shipping_address2 = models.CharField(max_length=255)
    shipping_area_building = models.CharField(max_length=255)
    shipping_landmark = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255)
    shipping_pincode = models.IntegerField()
    shipping_country = models.CharField(max_length=255)
    types = models.CharField(max_length=255,choices=TYPE_CHOICES)
    company_platform = models.CharField(max_length=255)


