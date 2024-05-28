from django.shortcuts import render, redirect
from .models import CompanyRecommendation
from .utils import google_search, extract_contact_info

def search_and_enhance(request):
    if request.method == "POST":
        search_query = request.POST.get('search_term')

        results = google_search(search_query)

        enhanced_results = []
        for result in results:
            website_url = result['link']
            contact_link, emails, company_name, phone_number = extract_contact_info(website_url)
            try:
                company_recommendation = CompanyRecommendation(
                    website_url=website_url,
                    company_name=company_name,
                    emails=emails,
                    contact_link=contact_link,
                    phone_number=phone_number
                )
                company_recommendation.save()
            except Exception as e:
                print(f"Error saving data for {website_url}:", e)

            enhanced_results.append({
                'website_url': website_url,
                'contact_link': contact_link,
                'emails': emails,
                'phone_number': phone_number,
                'company_name': company_name
            })



        context = {'results': enhanced_results, 'search_query': search_query}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'search_form.html')
