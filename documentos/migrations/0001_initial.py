# Generated by Django 5.2.1 on 2025-05-23 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FluxoPredefinido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GrupoPermissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cor', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StatusProcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoProcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_processo', models.CharField(max_length=100)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('assunto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.assunto')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.statusprocesso')),
                ('tipo_processo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.tipoprocesso')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('caminho_arquivo', models.CharField(max_length=500)),
                ('versao_atual', models.IntegerField()),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.processo')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.statusdocumento')),
                ('tipo_documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.tipodocumento')),
            ],
        ),
        migrations.CreateModel(
            name='EtapaFluxo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.IntegerField()),
                ('acao_esperada', models.CharField(max_length=255)),
                ('fluxo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.fluxopredefinido')),
                ('setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.setor')),
            ],
        ),
        migrations.CreateModel(
            name='CaixaEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('data_entrada', models.DateTimeField(auto_now_add=True)),
                ('lido', models.BooleanField(default=False)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.setor')),
            ],
        ),
        migrations.CreateModel(
            name='PermissaoSetorDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pode_criar', models.BooleanField(default=False)),
                ('pode_visualizar', models.BooleanField(default=False)),
                ('pode_editar', models.BooleanField(default=False)),
                ('pode_assinar', models.BooleanField(default=False)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.setor')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.tipodocumento')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('is_ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.setor')),
            ],
        ),
        migrations.AddField(
            model_name='processo',
            name='criado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.usuario'),
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('lida', models.BooleanField(default=False)),
                ('tipo', models.CharField(max_length=50)),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_envio', models.DateTimeField()),
                ('data_recebimento', models.DateTimeField(blank=True, null=True)),
                ('observacao', models.TextField()),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
                ('de_setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimentos_saida', to='documentos.setor')),
                ('para_setor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movimentos_entrada', to='documentos.setor')),
                ('usuario_responsavel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='LogSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.TextField()),
                ('objeto_afetado', models.CharField(max_length=255)),
                ('objeto_id', models.IntegerField()),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='AssinaturaDigital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado_digital', models.TextField()),
                ('data_assinatura', models.DateTimeField()),
                ('tipo_assinatura', models.CharField(max_length=50)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.grupopermissao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='VersaoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_versao', models.IntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('caminho_arquivo', models.CharField(max_length=500)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentos.usuario')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
            ],
        ),
    ]
