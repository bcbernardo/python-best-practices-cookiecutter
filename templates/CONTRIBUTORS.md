<!--
{%- for author_info in authors -%}
SPDX-FileCopyrightText: {{copyright_years}} {{author_info}}
{%- endfor %}

SPDX-License-Identifier: {{project_license}}
-->

# {{project_name}} contributors

{% if (authors|length) == 0 %}
This package have no contributors yet. Check our [contributing guidelines][] and be the first!
{% else %}
The following people have took the time to contribute and improve **{{project_name}}**. Thank you very much!

{% for contributor in contributors %}
- {{contributor["name"]}} ([@{{contributer["login"]}}]({{contributer["url"]}}))
{% endfor %}

Check our [contributing guidelines][] and contribute you too!
{% endif %}

[contributing guidelines]: {{documentation_url}}/contribute/CONTRIBUTING.md
