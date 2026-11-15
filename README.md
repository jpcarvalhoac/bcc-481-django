# demo-django

**Aluno:** João Pedro Andrade Carvalho
**Matrícula:** 22.2.4075
**Curso:** Ciência da Computação

---

Site simples em **Django 5.1** + **Tailwind CSS** (CDN) + **SQLite**, executado em **Docker**.

## Executar

```bash
docker compose up --build
```

Acesse http://localhost:8000

## Criar o usuário admin

Com o servidor rodando, em outro terminal:

```bash
docker compose exec web python manage.py createsuperuser
```

Painel: http://localhost:8000/admin/

## Migrations (após alterar models)

```bash
docker compose run --rm web python manage.py makemigrations
docker compose run --rm web python manage.py migrate
```

## Popular o banco com dados de exemplo (opcional)

```bash
docker compose exec web python manage.py seed
```

Também é possível inserir dados pelo shell do Django:

```bash
docker compose exec web python manage.py shell
```

## Parar

`Ctrl+C` e, para remover o container: `docker compose down`
