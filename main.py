import flet as ft
from auth import authenticate

def main(page: ft.Page):
    page.title = "Login Page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_100
    
    try:
        _ = page.session.get("logged_in")
        
    except KeyError:
        page.session.set("logged_in", False)
    
    
    def login_page():
        username_input = ft.TextField(label="Username", hint_text="Ex. apple@gmail.com", width=200)
        password_input = ft.TextField(label="Password", hint_text="Enter your passward", width=300, password=True)
        
        # Message label
        message = ft.Text(value="", color="red")
        
        #Login button click event handler
        def login_click(e):
            username = username_input.value
            password = password_input.value
            
            if authenticate(username, password):
                page.session.set("logged_in", True)
                page.go("/home")
            else:
                message.value = "Login Failed!! Invalid username or password"
                message.color = "red"
            page.update()
        
        login_button = ft.ElevatedButton(text="Login", width=400, on_click=login_click)
        
        # Container with custom background color
        container = ft.Container(
            content=ft.Column(
                [
                    username_input,
                    password_input,
                    login_button,
                    message,
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.WHITE,
            padding=20,
            border_radius=10,
        )
        
        # Add the container to the page
        return ft.Container(
            content=container,
            alignment=ft.alignment.center,
            expand=True,
        )
        
    def authentification_check():
        username_input = ft.TextField(label="Username", hint_text="Ex. apple@gmail.com", width=200)
        password_input = ft.TextField(label="Password", hint_text="Enter your password", width=300, password=True)
        
        message = ft.Text(value="", color="red")
        
        def login_click(e):
            username = username_input.value
            password = password_input.value
            
            if authenticate(username, password):
                page.session.set("logged_in", True)
                page.go("/home")
            else:
                message.value = "Re-Login Failed!! Invalid username or password"
                message.color = "red"
            page.update()
        
        login_button = ft.ElevatedButton(text="Authentification Check", width=400, on_click=login_click)
        
        container = ft.Container(
            content=ft.Column(
                [
                    username_input,
                    password_input,
                    login_button,
                    message,
                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.WHITE,
            padding=20,
            border_radius=10,
        )
        
        return ft.Container(
            content=container,
            alignment=ft.alignment.center,
            expand=True,
        )
        
        
    def hompage():
        def logout_click(e):
            page.session.set("logged_in", False)
            page.go("/login")
        
        logout_button = ft.ElevatedButton(text="Logout", on_click=logout_click)
        
        return ft.Container(
            content=ft.Stack(
                [   
                    ft.Container(
                        content=ft.Text(value="Welcome to Home Page", size=50),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=logout_button,
                        alignment=ft.alignment.top_right,
                        padding=ft.Padding(10, 10, 10, 10),
                    ),
                ]
            ),
            alignment=ft.alignment.center,
            expand=True,
        )
        
    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            if page.session.get("logged_in"):
                page.views.append(ft.View(route, [hompage()]))
                page.session.set("logged_in", False)
            else:
                page.views.append(ft.View(route, [authentification_check()]))
        elif page.route == "/login":
            page.views.append(ft.View(route, [login_page()]))
        else: 
            page.views.append(ft.View(route, [login_page()]))
        page.update()
    
        
    page.on_route_change = route_change
    page.go("/login")
     

ft.app(target=main)
