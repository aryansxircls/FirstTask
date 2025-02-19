# Generated by Django 3.2.12 on 2024-04-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_code', models.IntegerField()),
                ('children', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('cust_status', models.CharField(choices=[('Open', 'Open'), ('Contacted', 'Contacted'), ('Qualified', 'Qualified'), ('Unqualified', 'Unqualified')], max_length=255)),
                ('cust_source', models.CharField(choices=[('Networking', 'Networking'), ('Phone Enquiry', 'Phone Enquiry'), ('Cold Call', 'Cold Call'), ('Cold Email', 'Cold Email'), ('Trade Show', 'Trade Show'), ('Employee Referral', 'Employee Referral'), ('Client Referral', 'Client Referral'), ('External Referral', 'External Referral'), ('SEO/SEM Campaign', 'SEO/SEM Campaign'), ('Email Marketing Campaign', 'Email Marketing Campaign'), ('Web-Contact Form', 'Web-Contact Form'), ('Web-Enquiry Form', 'Web-Enquiry Form'), ('Web-Search', 'Web-Search'), ('Webinar', 'Webinar'), ('Other', 'Other')], max_length=255)),
                ('cust_rating', models.CharField(choices=[('Cold', 'Cold'), ('Warm', 'Warm'), ('Hot', 'Hot')], max_length=255)),
                ('cust_lead', models.CharField(choices=[('Lead Stage', 'Lead Stage'), ('2', 'Prospect'), ('3', 'Presentation/Pitch'), ('4', 'Demo'), ('5', 'Planning'), ('9', 'Query Solving'), ('10', 'Request for Proposal'), ('11', 'Negotiation'), ('12', 'LOI/Heads of Terms'), ('13', 'Signed Agreement'), ('14', 'Invoice Raised'), ('15', 'Signed Up'), ('16', 'Add Company'), ('17', 'Add Outlet'), ('18', 'Offers Designed'), ('19', 'Campaign Created'), ('20', 'Plugin Integration'), ('21', 'Campaign Live'), ('22', 'Offers Active'), ('23', 'DNS Integration'), ('24', 'Customer'), ('25', 'Single Offer Created'), ('26', 'Parked Funnel')], max_length=255)),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Miss', 'Miss'), ('Ms.', 'Ms.')], max_length=255)),
                ('cust_first_name', models.CharField(max_length=255)),
                ('cust_last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_no', models.IntegerField()),
                ('phone_no2', models.IntegerField()),
                ('landline1', models.IntegerField()),
                ('landline2', models.IntegerField()),
                ('cust_dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=255)),
                ('martial_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], max_length=255)),
                ('no_of_children', models.IntegerField()),
                ('occupation', models.CharField(choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Student', 'Student'), ('Unemployed', 'Unemployed')], max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('lead_social_twitter', models.CharField(max_length=255)),
                ('lead_social_fb', models.CharField(max_length=255)),
                ('lead_social_insta', models.CharField(max_length=255)),
                ('lead_social_linkedin', models.CharField(max_length=255)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('area_building', models.CharField(max_length=255)),
                ('landmark', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('shipping_address1', models.CharField(max_length=255)),
                ('shipping_address2', models.CharField(max_length=255)),
                ('shipping_area_building', models.CharField(max_length=255)),
                ('shipping_landmark', models.CharField(max_length=255)),
                ('shipping_city', models.CharField(max_length=255)),
                ('shipping_state', models.CharField(max_length=255)),
                ('shipping_pincode', models.IntegerField()),
                ('shipping_country', models.CharField(max_length=255)),
                ('types', models.CharField(choices=[('RETAIL', 'Retail')], max_length=255)),
                ('company_platform', models.CharField(max_length=255)),
            ],
        ),
    ]
