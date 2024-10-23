# -*- coding: utf-8 -*-
# © 2024 Sergio Martínez Meneses
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Historial Clínico',
    'summary': 'Gestión y seguimiento del historial clínico de clientes.',
    'author': 'Sergio Martinez Meneses',
    'company': 'Quetzalcode',
    'maintainer': 'Sergio Martinez Meneses',
    'website': 'https://sergiommq.github.io/portafolio/',
    'category': 'Soporte Técnico',
    'version': '1.0.0',
    'description': """
        La aplicación Historial Clínico permite gestionar de manera eficiente el historial médico 
        de los clientes. Los datos se enlazan directamente a los contactos, proporcionando un acceso 
        rápido y claro a la información médica esencial de cada cliente.
    """,
    'depends': ['base', 'contacts'],  
    'data': [
        'security/ir.model.access.csv',
        'views/clinical_history_views.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'price': 50.00,
    'currency': 'USD',
    'support': 'quetzal.mq97@gmail.com',
}
