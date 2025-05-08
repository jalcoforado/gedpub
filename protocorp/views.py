from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Bem-vindo ao GEDPub 🚀</h1>
        <p>Este é o sistema de gestão de processos e documentos da prefeitura.</p>
        <ul>
            <li><a href="/admin/">Acessar Admin</a></li>
            <li><a href="/api/processos/">Ver Processos</a></li>
            <li><a href="/api/tramites/">Ver Tramitações</a></li>
        </ul>
    """)
