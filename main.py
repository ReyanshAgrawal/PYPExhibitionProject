from nicegui import ui
from shared import core
import os

@ui.page('/adminsite')
def main():
    ui.label("Admin Site")
    login_container = ui.column()
    access_container = ui.column().classes('hidden')

    with login_container:
        username = ui.input("Username")
        pass_ = ui.input("Password", password=True)
        def on_submit():
            if username.value == "admin.RAReyanshAgrawal" and pass_.value == "password.ohCoderngaming":
                login_container.classes('hidden')
                access_container.classes(remove='hidden')
                show_access_controls()
            else:
                ui.notify("Access Denied", color="red")
        ui.button("Submit", on_click=on_submit)

    def show_access_controls():
        with access_container:
            toggle = ui.switch("Site Access")
            status_label = ui.label()
            def updateFlag():
                core.set_flag("site_open", toggle.value)
                status_label.text = "Site Open" if toggle.value else "Site Closed"
                status_label.classes(remove="text-green-600")
                status_label.classes(remove="text-red-600")
                status_label.classes(add="text-green-600" if toggle.value else "text-red-600")
            toggle.on_value_change(updateFlag)
            updateFlag()

@ui.page("/usersite")
def main():
    ui.label("User Site")

    login_container = ui.column().classes("hidden")
    pledge_container = ui.column().classes("hidden")

    def show_login():
        with login_container:
            username = ui.input("Username")
            pass_ = ui.input("Password", password=True)

            def on_submit():
                if username.value == "admin.RAReyanshAgrawal" and pass_.value == "password.ohCoderngaming":
                    ui.notify("Access Granted", color="green")
                    login_container.classes('hidden')
                    pledge_container.classes(remove='hidden')
                    show_pledge_stuff()
                else:
                    ui.notify("Access Denied", color="red")

            ui.button("Submit", on_click=on_submit)

    def show_pledge_stuff():
        with pledge_container:
            username = ui.input("Username")
            pledge = ui.textarea("Pledge")

            def on_submit():
                if not username.value.strip():
                    ui.notify("Username is required", color="red")
                    return
                if not pledge.value.strip():
                    ui.notify("Pledge is required", color="red")
                    return

                core.add_pledge(username.value, pledge.value)
                ui.notify("Pledge submitted successfully!", color="green")

            ui.button("Submit", on_click=on_submit)

    if not core.get_flag("site_open"):
        login_container.classes(remove="hidden")
        show_login()
    else:
        pledge_container.classes(remove="hidden")
        show_pledge_stuff()


ui.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))