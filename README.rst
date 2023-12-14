=============================
Django Bootstrap Forms (NVS)
=============================

|Latest Version|  |Downloads|  |License|

Django Bootstrap Forms is a Django app that provides enhanced form rendering with Bootstrap styles.

Installation
------------

1. Install the package using pip:

    .. code-block:: bash
    
       pip install nvs-bootstrap-forms

2. Add 'bootstrap_forms' to your `INSTALLED_APPS` in the Django settings:

    .. code-block:: python
    
       INSTALLED_APPS = [
           # ...
           'bootstrap_forms',
           # ...
       ]
       
3. Include Bootstraps css and js links in your html:

    .. code-block:: html
    
        <!doctype html>
        <html lang="en">
          <head>
            <!-- Your headers goes here -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
          </head>
          <body>
            <!-- Your content goes here -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
          </body>
        </html>


Usage
-----

1. **Load Bootstrap Forms in your template:**

   .. code-block:: html+django

      {% load bootstrap_forms_tags %}

2. **Use the `bootstrap_form` template tag to render your form:**

   .. code-block:: html+django

      <form method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
        <button type="submit">Submit</button>
      </form>

   This will render the form with Bootstrap styles.

3. **Customization:**

   - You can customize the rendering of individual fields by using the `field_order` and other attributes in your form fields.

   - For advanced customization, you can extend the provided `BootstrapFormRendererNode` class in the `bootstrap_forms.templatetags.bootstrap_forms_tags` module.

Contributing
------------

Feel free to contribute by opening issues or submitting pull requests. Please read the `Contributing Guidelines <CONTRIBUTING.md>`_ for more details.

License
-------

This project is licensed under the MIT License - see the `LICENSE <LICENSE.md>`_ file for details.

.. |Latest Version| image:: https://img.shields.io/pypi/v/django-bootstrap-forms.svg
   :target: https://pypi.python.org/pypi/django-bootstrap-forms
   :alt: Latest Version

.. |Downloads| image:: https://img.shields.io/pypi/dm/django-bootstrap-forms.svg
   :target: https://pypi.python.org/pypi/django-bootstrap-forms
   :alt: Downloads

.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :alt: License
   :target: https://opensource.org/licenses/MIT
