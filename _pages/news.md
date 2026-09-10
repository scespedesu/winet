---
layout: single
title: "News"
permalink: /news/
---

<ul class="news-list">
{% assign news_items = site.news | sort: "date" | reverse %}
{% for item in news_items %}
  <li>
    <span class="news-date">{{ item.date | date: "%B %Y" }}</span> —
    <strong>{{ item.title }}</strong>
    {% if item.content and item.content != "" %}<br>{{ item.content }}{% endif %}
  </li>
{% endfor %}
</ul>

---

News from 2014–2020 (Universidad de Chile era) is preserved on the [2014–2022 archive]({{ '/legacy-uchile/index.html' | relative_url }}).
