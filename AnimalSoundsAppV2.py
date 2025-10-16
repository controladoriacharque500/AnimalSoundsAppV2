import flet as ft
import os

# --- 1. Função de Reprodução de Áudio e Criação de Botão ---
# No Flet, a reprodução de áudio é gerenciada por um controle 'Audio' adicionado à página.

def create_animal_button(animal_name, page: ft.Page):
    """Cria um botão de imagem que reproduz o som correspondente."""

    # URL relativo à pasta 'assets' que será incluída no build
    image_path = f"assets/images/{animal_name}.png"
    sound_path = f"assets/sounds/{animal_name}.wav"

    # Verifica se o arquivo de som existe na pasta assets
    if not os.path.exists(sound_path):
        print(f"AVISO: Arquivo de som não encontrado em: {sound_path}")
        return ft.Container() # Retorna um container vazio se o som não existir

    # Cria o controle de áudio
    audio_player = ft.Audio(
        src=sound_path,
        volume=1,
        autoplay=False
    )

    # Adiciona o controle de áudio à sobreposição da página (necessário para que funcione)
    page.overlay.append(audio_player)

    # Cria o widget de imagem
    animal_image = ft.Image(
        src=image_path,
        fit=ft.ImageFit.COVER,
    )

    # O Flet usa um Container com GestureDetector para criar um 'botão' clicável com uma imagem
    # O 'on_click' substitui o 'bind(on_press=...)' do Kivy
    return ft.Container(
        content=animal_image,
        width=150,
        height=150,
        alignment=ft.alignment.center,
        on_click=lambda e: audio_player.play(), # Reproduz o som ao clicar
        border_radius=ft.border_radius.all(10),
        bgcolor=ft.Colors.BLACK12 # Um fundo sutil para visibilidade
    )


# --- 2. Função Principal do Aplicativo (Substitui AnimalSoundsApp.build) ---

def main(page: ft.Page):
    page.title = "Sons de Animais Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    # Lista de animais (a mesma do seu código Kivy)
    animais = ['cao', 'gato', 'leao', 'elefante', 'macaco', 'pato']

    # Substitui o GridLayout(cols=3) do Kivy pelo GridView do Flet
    # O GridView é ideal para grades com número fixo de colunas
    grid_view = ft.GridView(
        runs_count=3, # Equivalente ao cols=3 do GridLayout
        spacing=10,
        run_spacing=10,
        child_aspect_ratio=1.0, # Mantém os itens quadrados
        expand=True,
    )

    # Adiciona os botões de animais ao GridView
    for animal in animais:
        btn = create_animal_button(animal, page)
        grid_view.controls.append(btn)

    # Adiciona o GridView à página
    page.add(grid_view)

    # A função main deve ser sempre atualizada no final
    page.update()

# --- 3. Execução do Aplicativo (Substitui if __name__ == '__main__':) ---

if __name__ == "__main__":
    # Configura o aplicativo para ser executado no modo desktop/móvel
    ft.app(target=main, assets_dir="assets")
