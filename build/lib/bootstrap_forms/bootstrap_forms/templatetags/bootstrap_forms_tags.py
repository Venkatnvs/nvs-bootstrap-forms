from django import template

register = template.Library()

class BootstrapFormRendererNode(template.Node):
    def __init__(self, form):
        self.form = template.Variable(form)

    def render(self, context):
        form = self.form.resolve(context)
        if form is None:
            raise ValueError("The 'form' cannot be None.")
        html_code = self.get_code(form)
        # html_code = form.as_p()
        return html_code

    def get_code(self, form):
        sorted_fields = sorted(form, key=lambda field: getattr(field.field.widget.attrs, 'field_order', 0))
        rendered_fields = [self.render_field(field) for field in sorted_fields]
        code = '\n'.join(rendered_fields)
        return f"""
            {self.render_ctm_css()}\n{code}
        """

    def render_field(self, field):
        input_type = field.field.widget.input_type
        if input_type == 'checkbox':
            return self.render_checkbox_field(field)
        elif input_type == 'select':
            return self.render_select_field(field)
        elif input_type == 'text':
            return self.render_text_field(field)
        elif input_type == 'textarea':
            return self.render_textarea_field(field)
        elif input_type == 'radio':
            return self.render_radio_field(field)
        elif input_type == 'password':
            return self.render_password_field(field)
        elif input_type == 'email':
            return self.render_email_field(field)
        elif input_type == 'number':
            return self.render_number_field(field)
        elif input_type == 'date':
            return self.render_date_field(field)
        elif input_type == 'file':
            return self.render_file_field(field)
        elif input_type == 'url':
            return self.render_url_field(field)
        elif input_type == 'color':
            return self.render_color_field(field)
        elif input_type == 'tel':
            return self.render_tel_field(field)
        else:
            return self.render_default_field(field)

    def render_checkbox_field(self, field):
        return f"""
            <div class="mt-2 form-check form-switch">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-check-input">
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_select_field(self, field):
        if field.field.widget.allow_multiple_selected:
            return self.render_multiple_select_field(field)
        else:
            return self.render_single_select_field(field)

    def render_single_select_field(self, field):
        options = '\n'.join([f'<option value="{id}">{value}</option>' for id, value in field.field.choices])
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <select id="id_{field.name}" name="{field.name}" class="form-select">
                    {options}
                </select>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_multiple_select_field(self, field):
        options = '\n'.join([f'<option value="{id}">{value}</option>' for id, value in field.field.choices])
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <select id="id_{field.name}" name="{field.name}" class="form-select" multiple>
                    {options}
                </select>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_default_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """
    
    def render_text_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """
    
    def render_textarea_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <textarea id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}></textarea>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """
    
    def render_radio_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                {field.field.widget.render(name=field.name, value=field.value, attrs={'class': 'form-radio'})}
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """
    
    def render_password_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """
    
    def render_email_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_number_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_date_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_file_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """
    
    def render_url_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input required type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_color_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input required type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """

    def render_tel_field(self, field):
        return f"""
            <div class="mt-2 form-group">
                {self.render_label(field)}
                <input required type="{field.field.widget.input_type}" id="id_{field.name}" name="{field.name}" class="form-control" {self.render_placeholder(field)}>
                {self.render_help_text(field)}
                {self.render_errors(field)}
            </div>
        """
    
    def render_label(self, field):
        return field.label_tag()
    
    def render_placeholder(self, field):
        placeholder = field.field.widget.attrs.get('placeholder', '')
        return f'placeholder="{placeholder}"' if placeholder else ''

    def render_help_text(self, field):
        return f'<span><small class="text-muted">{field.help_text}</small></span>'

    def render_errors(self, field):
        if field.errors:
            return f'<div class="alert alert-danger m-0 p-0 pt-1 rounded-1">{field.errors}</div>'
        return ''
    
    def render_ctm_css(self):
        return """
            <style>
                .form-control {
                    border-radius: 3px;
                }
            </style>
        """

@register.tag
def bootstrap_form(parser, token):
    try:
        tag_name, form = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(f"{token.contents} tag requires a form argument.")
    
    return BootstrapFormRendererNode(form)