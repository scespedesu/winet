---
layout: single
title: "Publications"
permalink: /publications/
---

<div class="notice--warning" markdown="1">
**Draft list — please review.** The entries below were compiled automatically from public indexes (ResearchGate/Google Scholar) as a starting point. Titles, venues, and years should be correct, but full author order has **not** been verified for every entry — check each one (especially author order and any listed as "et al.") before treating this as final. See the repo's `README.md` ("Adding a publication") for how to edit or add entries.
</div>

{% assign pubs_by_year = site.publications | group_by: "year" | sort: "name" | reverse %}
{% for year_group in pubs_by_year %}
### {{ year_group.name }}

<ul class="publication-list">
{% assign year_pubs = year_group.items | sort: "title" %}
{% for pub in year_pubs %}
  <li>
    {{ pub.authors }}. <strong>{{ pub.title }}</strong>. <em>{{ pub.venue }}</em>{% if pub.verified == false %} <span class="pub-flag" title="Author list not yet verified">[verify]</span>{% endif %}.
    {% if pub.links %}
      {% if pub.links.doi %} [[DOI]]({{ pub.links.doi }}){% endif %}
      {% if pub.links.pdf %} [[PDF]]({{ pub.links.pdf }}){% endif %}
      {% if pub.links.arxiv %} [[arXiv]]({{ pub.links.arxiv }}){% endif %}
    {% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}

---

Older publications (2020 and earlier) from the group's time at Universidad de Chile are listed on the [2014–2022 archive]({{ '/legacy-uchile/index.html' | relative_url }}).
