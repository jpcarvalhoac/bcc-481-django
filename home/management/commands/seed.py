from django.core.management.base import BaseCommand

from home.models import Categoria, Mensagem, Tag


class Command(BaseCommand):
    help = "Popula o banco com categorias, tags e mensagens de exemplo (idempotente)."

    def handle(self, *args, **options):
        categorias = {
            nome: Categoria.objects.get_or_create(nome=nome)[0]
            for nome in ["Aviso", "Dúvida", "Sugestão"]
        }
        tags = {
            nome: Tag.objects.get_or_create(nome=nome)[0]
            for nome in ["django", "tutorial", "iniciante", "docker", "orm"]
        }

        dados = [
            (
                "Bem-vindo ao demo-django",
                "Primeira mensagem criada via código Python, sem usar o admin.",
                "Professor",
                "Aviso",
                ["django", "tutorial", "iniciante"],
            ),
            (
                "Como subir o projeto com Docker?",
                "Basta rodar docker compose up --build na raiz do projeto.",
                "Aluno",
                "Dúvida",
                ["docker", "iniciante"],
            ),
            (
                "Explorar o ORM no shell",
                "Que tal praticar consultas com Mensagem.objects e tag.mensagens.all()?",
                "Monitor",
                "Sugestão",
                ["django", "orm"],
            ),
        ]

        for titulo, conteudo, autor, categoria, nomes_tags in dados:
            mensagem, criada = Mensagem.objects.get_or_create(
                titulo=titulo,
                defaults={
                    "conteudo": conteudo,
                    "autor": autor,
                    "categoria": categorias[categoria],
                },
            )
            mensagem.tags.add(*[tags[n] for n in nomes_tags])
            self.stdout.write(
                f"{'Criada' if criada else 'Já existia'}: {mensagem.titulo} "
                f"({mensagem.tags.count()} tags)"
            )

        self.stdout.write(self.style.SUCCESS("Seed concluído."))
