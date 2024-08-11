"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .components import navbar, sidebar_with_user_profile

class State(rx.State):
    """The app state."""
    color = "green"
    title = "Welcome to PostIn!"

    def change_bg_on_hover(self):
        if self.color == "green":
            self.color = "red"
        else:
            self.color = "green"

    def handle_title_input_change(self, value):
        self.title = value


def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        # sidebar_with_user_profile(),
        rx.box(
            child,
            bg=rx.color("white", 3),
            padding="1em",
            width="100%",
        ),
        rx.color_mode.button(position="bottom-left"),
        
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.title, size="9", color=State.color),
            rx.chakra.input(default_value=State.title, on_change=State.handle_title_input_change),
            rx.button("Click me", on_click=State.change_bg_on_hover),
            rx.link(
                rx.button("Check out our API docs!", bg=State.color),
                href=f"{config.base_url}/docs",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
