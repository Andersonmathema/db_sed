import scrapy
from scrapy.http import FormRequest

class LoginSedSpider(scrapy.Spider):
    name = 'login_sed'
    start_urls = ['https://sed.educacao.sp.gov.br']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'name': 'rg466709742sp',
                'senha': '@Antero89'                
            },
            callback=self.after_login
        )
    
    def after_login(self, response):
        return scrapy.Request(
            url='https://sed.educacao.sp.gov.br/Aluno/GridAcesso',
            callback=self.parse_table
        )
    

    def parse_table(self, response):
        # Lógica para extrair os dados da tabela
        rows = response.xpath('//table/tr')

        ## REVER AQUI, como acessar paginas escondidas ao clicar na sala
        for row in rows:
            item = {
                'column1': row.xpath('td[1]/text()').get(),
                'column2': row.xpath('td[2]/text()').get(),
                # Adicione mais colunas conforme necessário
            }
            yield item

