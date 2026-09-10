---
layout: single
title: "People"
permalink: /people/
---

<div class="notice--warning" markdown="1">
**Placeholder roster.** Only the PI and one example entry are filled in below — the group's actual current members and alumni list needs to be added. See the repo's `README.md` ("Adding a person") for the quick copy-paste format.
</div>

## Principal Investigator

{% assign pi = site.people | where: "role", "Principal Investigator" | first %}
{% if pi %}
**{{ pi.name }}** — [{{ pi.title }}]({{ pi.website }})
{% endif %}

## Current members

<ul>
{% assign current_people = site.people | where: "status", "current" | where_exp: "p", "p.role != 'Principal Investigator'" | sort: "role" %}
{% for p in current_people %}
  <li><strong>{{ p.name }}</strong> — {{ p.role }}{% if p.thesis %}, <em>{{ p.thesis }}</em>{% endif %}</li>
{% endfor %}
</ul>

## Alumni

<ul>
{% assign alumni = site.people | where: "status", "alumni" | sort: "name" %}
{% for p in alumni %}
  <li><strong>{{ p.name }}</strong> — {{ p.role }}{% if p.now %}, now {{ p.now }}{% endif %}</li>
{% endfor %}
</ul>
