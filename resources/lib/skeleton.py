# -*- coding: utf-8 -*-
"""
    Catch-up TV & More
    Copyright (C) 2016  SylvainCecchetto

    This file is part of Catch-up TV & More.

    Catch-up TV & More is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Catch-up TV & More is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with Catch-up TV & More; if not, write to the Free Software Foundation,
    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# The unicode_literals import only has
# an effect on Python 2.
# It makes string literals as unicode like in Python 3
from __future__ import unicode_literals
from codequick import Script


"""
The following dictionaries describe
the addon's tree architecture.
* Key: item id
* Value: item infos
    - callback: Callback function to run once this item is selected
    - thumb: Item thumb path relative to "media" folder
    - fanart: Item fanart path relative to "meia" folder
    - module: Item module to load in order to work (like 6play.py)
"""

ROOT = {
    'live_tv': {
        'callback': 'generic_menu',
        'thumb': 'live_tv.png'
    },
    'replay': {
        'callback': 'generic_menu',
        'thumb': 'replay.png'
    },
    'websites': {
        'callback': 'generic_menu',
        'thumb': 'websites.png'
    },
    'favourites': {
        'callback': 'favourites',
        'thumb': 'favourites.png'
    }
}


LIVE_TV = {
    'fr_live': {
        'callback': 'tv_guide_menu' if Script.setting.get_boolean('tv_guide') else 'generic_menu',
        'thumb': 'channels/fr.png'
    },
    'be_live': {
        'callback': 'tv_guide_menu' if Script.setting.get_boolean('tv_guide') else 'generic_menu',
        'thumb': 'channels/be.png'
    },
    'ca_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/ca.png'
    },
    'ch_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/ch.png'
    },
    'uk_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/uk.png'
    },
    'wo_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/wo.png'
    },
    'us_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/us.png'
    },
    'pl_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/pl.png'
    },
    'es_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/es.png'
    },
    'jp_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/jp.png'
    },
    'tn_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/tn.png'
    },
    'it_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/it.png'
    },
    'nl_live': {
        'callback': 'generic_menu',
        'thumb': 'channels/nl.png'
    }
}


REPLAY = {
    'be_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/be.png'
    },
    'ca_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/ca.png'
    },
    'fr_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/fr.png'
    },
    'jp_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/jp.png'
    },
    'ch_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/ch.png'
    },
    'uk_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/uk.png'
    },
    'wo_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/wo.png'
    },
    'us_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/us.png'
    }
    #,
    #'es_replay': {
    #    'callback': 'generic_menu',
    #    'thumb': 'channels/es.png'
    #}
    ,
    'it_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/it.png'
    },
    'tn_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/tn.png'
    },
    'nl_replay': {
        'callback': 'generic_menu',
        'thumb': 'channels/nl.png'
    }
}


FR_LIVE = {
    'tf1': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/tf1.png',
        'fanart': 'channels/fr/tf1_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1',
        'xmltv_id': 'C192.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 1
    },
    'tmc': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/tmc.png',
        'fanart': 'channels/fr/tmc_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1',
        'xmltv_id': 'C195.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 10
    },
    'tf1-series-films': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/tf1seriesfilms.png',
        'fanart': 'channels/fr/tf1seriesfilms_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1',
        'xmltv_id': 'C1404.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 20
    },
    'tfx': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/tfx.png',
        'fanart': 'channels/fr/tfx_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1',
        'xmltv_id': 'C446.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 11
    },
    'rtl2': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/rtl2.png',
        'fanart': 'channels/fr/rtl2_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play',
        'm3u_group': 'Radio'
    },
    'fun_radio': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/funradio.png',
        'fanart': 'channels/fr/funradio_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play',
        'm3u_group': 'Radio'
    },
    'virginradiotv': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/virginradiotv.png',
        'fanart': 'channels/fr/virginradiotv_fanart.jpg',
        'module': 'resources.lib.channels.fr.virginradiotv',
        'm3u_group': 'Radio'
    },
    'viaoccitanie': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/viaoccitanie.png',
        'fanart': 'channels/fr/viaoccitanie_fanart.jpg',
        'module': 'resources.lib.channels.fr.via',
        'm3u_group': 'Région'
    },
    'lci': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/lci.png',
        'fanart': 'channels/fr/lci_fanart.jpg',
        'module': 'resources.lib.channels.fr.lci',
        'xmltv_id': 'C112.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 26
    },
    'antennereunion': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/antennereunion.png',
        'fanart': 'channels/fr/antennereunion_fanart.jpg',
        'module': 'resources.lib.channels.fr.antennereunion',
        'm3u_group': 'Région'
    },
    'gulli': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/gulli.png',
        'fanart': 'channels/fr/gulli_fanart.jpg',
        'module': 'resources.lib.channels.fr.gulli',
        'xmltv_id': 'C482.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 18
    },
    'canalplus': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/canalplus.png',
        'fanart': 'channels/fr/canalplus_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal',
        'xmltv_id': 'C34.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 4
    },
    'c8': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/c8.png',
        'fanart': 'channels/fr/c8_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal',
        'xmltv_id': 'C445.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 8
    },
    'cstar': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/cstar.png',
        'fanart': 'channels/fr/cstar_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal',
        'xmltv_id': 'C458.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 17
    },
    'france-2': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/france2.png',
        'fanart': 'channels/fr/france2_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv',
        'xmltv_id': 'C4.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 2
    },
    'france-3': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/france3.png',
        'fanart': 'channels/fr/france3_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv',
        'xmltv_id': 'C80.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 3
    },
    'france-4': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/france4.png',
        'fanart': 'channels/fr/france4_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv',
        'xmltv_id': 'C78.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 14
    },
    'france-5': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/france5.png',
        'fanart': 'channels/fr/france5_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv',
        'xmltv_id': 'C47.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 5
    },
    'france-o': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/franceo.png',
        'fanart': 'channels/fr/franceo_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv',
        'xmltv_id': 'C160.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 19
    },
    'lequipe': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/lequipe.png',
        'fanart': 'channels/fr/lequipe_fanart.jpg',
        'module': 'resources.lib.channels.fr.lequipe',
        'xmltv_id': 'C1401.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 21
    },
    'cnews': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/cnews.png',
        'fanart': 'channels/fr/cnews_fanart.jpg',
        'module': 'resources.lib.channels.fr.cnews',
        'xmltv_id': 'C226.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 16
    },
    'rmcdecouverte': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/rmcdecouverte.png',
        'fanart': 'channels/fr/rmcdecouverte_fanart.jpg',
        'module': 'resources.lib.channels.fr.rmcdecouverte',
        'xmltv_id': 'C1400.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 24
    },
    'rmcstory': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/rmcstory.png',
        'fanart': 'channels/fr/rmcstory_fanart.jpg',
        'module': 'resources.lib.channels.fr.rmcstory',
        'xmltv_id': 'C1402.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 23
    },
    'canal10': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/canal10.png',
        'fanart': 'channels/fr/canal10_fanart.jpg',
        'module': 'resources.lib.channels.fr.canal10',
        'm3u_group': 'Région'
    },
    'nrj12': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/nrj12.png',
        'fanart': 'channels/fr/nrj12_fanart.jpg',
        'module': 'resources.lib.channels.fr.nrj',
        'xmltv_id': 'C444.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 12
    },
    'cherie25': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/cherie25.png',
        'fanart': 'channels/fr/cherie25_fanart.jpg',
        'module': 'resources.lib.channels.fr.nrj',
        'xmltv_id': 'C1399.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 25
    },
    'bfmparis': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/bfmparis.png',
        'fanart': 'channels/fr/bfmparis_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmparis',
        'm3u_group': 'Région'
    },
    'bfmtv': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/bfmtv.png',
        'fanart': 'channels/fr/bfmtv_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmtv',
        'xmltv_id': 'C481.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 15
    },
    'bfmbusiness': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/bfmbusiness.png',
        'fanart': 'channels/fr/bfmbusiness_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmtv',
        'xmltv_id': 'C1073.api.telerama.fr',
        'm3u_group': 'Satellite/FAI'
    },
    'gong': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/gong.png',
        'fanart': 'channels/fr/gong_fanart.jpg',
        'module': 'resources.lib.channels.fr.gong',
        'm3u_group': 'Satellite/FAI'
    },
    'la_1ere': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/la1ere.png',
        'fanart': 'channels/fr/la1ere_fanart.jpg',
        'module': 'resources.lib.channels.fr.la_1ere',
        'm3u_group': 'Région',
        'available_languages': [
            "Guadeloupe",
            "Guyane",
            "Martinique",
            "Mayotte",
            "Nouvelle Calédonie",
            "Polynésie",
            "Réunion",
            "St-Pierre et Miquelon",
            "Wallis et Futuna"
        ]
    },
    'kto': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/kto.png',
        'fanart': 'channels/fr/kto_fanart.jpg',
        'module': 'resources.lib.channels.fr.kto',
        'm3u_group': 'Satellite/FAI'
    },
    'ouatchtv': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/ouatchtv.png',
        'fanart': 'channels/fr/ouatchtv_fanart.jpg',
        'module': 'resources.lib.channels.fr.ouatchtv',
        'm3u_group': 'Satellite/FAI'
    },
    'publicsenat': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/publicsenat.png',
        'fanart': 'channels/fr/publicsenat_fanart.jpg',
        'module': 'resources.lib.channels.fr.publicsenat',
        'xmltv_id': 'C234.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 13
    },
    'lcp': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/lcp.png',
        'fanart': 'channels/fr/lcp_fanart.jpg',
        'module': 'resources.lib.channels.fr.lcp',
        'xmltv_id': 'C234.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 13
    },
    'francetvsport': {
        'callback': 'multi_live_bridge',
        'thumb': 'channels/fr/francetvsport.png',
        'fanart': 'channels/fr/francetvsport_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetvsport',
        'm3u_group': 'Satellite/FAI'
    },
    'franceinfo': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/franceinfo.png',
        'fanart': 'channels/fr/franceinfo_fanart.jpg',
        'module': 'resources.lib.channels.fr.franceinfo',
        'xmltv_id': 'C2111.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 27
    },
    'france3regions': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/france3regions.png',
        'fanart': 'channels/fr/france3regions_fanart.jpg',
        'module': 'resources.lib.channels.fr.france3regions',
        'm3u_group': 'Région',
        'available_languages': [
            'Alpes',
            'Alsace',
            'Aquitaine',
            'Auvergne',
            'Bourgogne',
            'Bretagne',
            'Centre-Val de Loire',
            'Chapagne-Ardenne',
            'Corse',
            "Côte d'Azur",
            'Franche-Compté',
            'Languedoc-Roussillon',
            'Limousin',
            'Lorraine',
            'Midi-Pyrénées',
            'Nord-Pas-de-Calais',
            'Basse-Normandie',
            'Haute-Normandie',
            'Paris Île-de-France',
            'Pays de la Loire',
            'Picardie',
            'Poitou-Charentes',
            'Provence-Alpes',
            'Rhône-Alpes'
        ]
    },
    'viaatv': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/viaatv.png',
        'fanart': 'channels/fr/viaatv_fanart.jpg',
        'module': 'resources.lib.channels.fr.via',
        'm3u_group': 'Région'
    },
    'viagrandparis': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/viagrandparis.png',
        'fanart': 'channels/fr/viagrandparis_fanart.jpg',
        'module': 'resources.lib.channels.fr.via',
        'm3u_group': 'Région'
    },
    'tebeo': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/tebeo.png',
        'fanart': 'channels/fr/tebeo_fanart.jpg',
        'module': 'resources.lib.channels.fr.tebeo',
        'm3u_group': 'Région'
    },
    'mb': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/mb.png',
        'fanart': 'channels/fr/mb_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play',
        'xmltv_id': 'C184.api.telerama.fr',
        'm3u_group': 'Satellite/FAI'
    },
    'm6': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/m6.png',
        'fanart': 'channels/fr/m6_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play',
        'xmltv_id': 'C118.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 6
    },
    'w9': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/w9.png',
        'fanart': 'channels/fr/w9_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play',
        'xmltv_id': 'C119.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 9
    },
    '6ter': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/6ter.png',
        'fanart': 'channels/fr/6ter_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play',
        'xmltv_id': 'C1403.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 22
    },
    'vialmtv': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/vialmtv.png',
        'fanart': 'channels/fr/vialmtv_fanart.jpg',
        'module': 'resources.lib.channels.fr.via',
        'm3u_group': 'Région'
    },
    'viamirabelle': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/viamirabelle.png',
        'fanart': 'channels/fr/viamirabelle_fanart.jpg',
        'module': 'resources.lib.channels.fr.via',
        'm3u_group': 'Région'
    },
    'viavosges': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/viavosges.png',
        'fanart': 'channels/fr/viavosges_fanart.jpg',
        'module': 'resources.lib.channels.fr.via',
        'm3u_group': 'Région'
    },
    'tl7': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/tl7.png',
        'fanart': 'channels/fr/tl7_fanart.jpg',
        'module': 'resources.lib.channels.fr.tl7',
        'm3u_group': 'Région'
    },
    'luckyjack': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/luckyjack.png',
        'fanart': 'channels/fr/luckyjack_fanart.jpg',
        'module': 'resources.lib.channels.fr.abweb',
        'm3u_group': 'Satellite/FAI'
    },
    'mblivetv': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/mblivetv.png',
        'fanart': 'channels/fr/mblivetv_fanart.jpg',
        'module': 'resources.lib.channels.fr.mblivetv',
        'm3u_group': 'Satellite/FAI'
    },
    'tv8montblanc': {
        'callback': 'live_bridge',
        'thumb': 'channels/fr/tv8montblanc.png',
        'fanart': 'channels/fr/tv8montblanc_fanart.jpg',
        'module': 'resources.lib.channels.fr.tv8montblanc',
        'm3u_group': 'Région'
    }
}

TN_LIVE = {
    'watania1': {
        'callback': 'live_bridge',
        'thumb': 'channels/tn/watania1.png',
        'fanart': 'channels/tn/watania1_fanart.jpg',
        'module': 'resources.lib.channels.tn.watania'
    },
    'watania2': {
        'callback': 'live_bridge',
        'thumb': 'channels/tn/watania2.png',
        'fanart': 'channels/tn/watania2_fanart.jpg',
        'module': 'resources.lib.channels.tn.watania'
    },
    'nessma': {
        'callback': 'live_bridge',
        'thumb': 'channels/tn/nessma.png',
        'fanart': 'channels/tn/nessma_fanart.jpg',
        'module': 'resources.lib.channels.tn.nessma'
    }
}

PL_LIVE = {
    'tvp3': {
        'callback': 'live_bridge',
        'thumb': 'channels/pl/tvp3.png',
        'fanart': 'channels/pl/tvp3_fanart.jpg',
        'module': 'resources.lib.channels.pl.tvp',
        'available_languages': [
            "Białystok",
            "Bydgoszcz",
            "Gdańsk",
            "Gorzów Wielkopolski",
            "Katowice",
            "Kielce",
            "Kraków",
            "Lublin",
            "Łódź",
            "Olsztyn",
            "Opole",
            "Poznań",
            "Rzeszów",
            "Szczecin",
            "Warszawa",
            "Wrocław"
        ]
    },
    'tvpinfo': {
        'callback': 'live_bridge',
        'thumb': 'channels/pl/tvpinfo.png',
        'fanart': 'channels/pl/tvpinfo_fanart.jpg',
        'module': 'resources.lib.channels.pl.tvp'
    },
    'tvppolonia': {
        'callback': 'live_bridge',
        'thumb': 'channels/pl/tvppolonia.png',
        'fanart': 'channels/pl/tvppolonia_fanart.jpg',
        'module': 'resources.lib.channels.pl.tvp'
    },
    'tvppolandin': {
        'callback': 'live_bridge',
        'thumb': 'channels/pl/tvppolandin.png',
        'fanart': 'channels/pl/tvppolandin_fanart.jpg',
        'module': 'resources.lib.channels.pl.tvp'
    }
}

ES_LIVE = {
    'realmadridtv': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/realmadridtv.png',
        'fanart': 'channels/es/realmadridtv_fanart.jpg',
        'module': 'resources.lib.channels.es.realmadridtv',
        'available_languages': ['EN', 'ES']
    },
    'antena3': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/antena3.png',
        'fanart': 'channels/es/antena3_fanart.jpg',
        'module': 'resources.lib.channels.es.atresplayer'
    },
    'lasexta': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/lasexta.png',
        'fanart': 'channels/es/lasexta_fanart.jpg',
        'module': 'resources.lib.channels.es.atresplayer'
    },
    'neox': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/neox.png',
        'fanart': 'channels/es/neox_fanart.jpg',
        'module': 'resources.lib.channels.es.atresplayer'
    },
    'nova': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/nova.png',
        'fanart': 'channels/es/nova_fanart.jpg',
        'module': 'resources.lib.channels.es.atresplayer'
    },
    'mega': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/mega.png',
        'fanart': 'channels/es/mega_fanart.jpg',
        'module': 'resources.lib.channels.es.atresplayer'
    },
    'atreseries': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/atreseries.png',
        'fanart': 'channels/es/atreseries_fanart.jpg',
        'module': 'resources.lib.channels.es.atresplayer'
    },
    'telecinco': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/telecinco.png',
        'fanart': 'channels/es/telecinco_fanart.jpg',
        'module': 'resources.lib.channels.es.mitele'
    },
    'cuatro': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/cuatro.png',
        'fanart': 'channels/es/cuatro_fanart.jpg',
        'module': 'resources.lib.channels.es.mitele'
    },
    'fdf': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/fdf.png',
        'fanart': 'channels/es/fdf_fanart.jpg',
        'module': 'resources.lib.channels.es.mitele'
    },
    'boing': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/boing.png',
        'fanart': 'channels/es/boing_fanart.jpg',
        'module': 'resources.lib.channels.es.mitele'
    },
    'energy': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/energy.png',
        'fanart': 'channels/es/energy_fanart.jpg',
        'module': 'resources.lib.channels.es.mitele'
    },
    'divinity': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/divinity.png',
        'fanart': 'channels/es/divinity_fanart.jpg',
        'module': 'resources.lib.channels.es.mitele'
    },
    'bemad': {
        'callback': 'live_bridge',
        'thumb': 'channels/es/bemad.png',
        'fanart': 'channels/es/bemad_fanart.jpg',
        'module': 'resources.lib.channels.es.mitele'
    }
}

WO_LIVE = {
    'tivi5monde': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/tivi5monde.png',
        'fanart': 'channels/wo/tivi5monde_fanart.jpg',
        'module': 'resources.lib.channels.wo.tivi5monde'
    },
    'tv5mondefbs': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/tv5mondefbs.png',
        'fanart': 'channels/wo/tv5mondefbs_fanart.jpg',
        'module': 'resources.lib.channels.wo.tv5monde'
    },
    'tv5mondeinfo': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/tv5mondeinfo.png',
        'fanart': 'channels/wo/tv5mondeinfo_fanart.jpg',
        'module': 'resources.lib.channels.wo.tv5monde'
    },
    'euronews': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/euronews.png',
        'fanart': 'channels/wo/euronews_fanart.jpg',
        'module': 'resources.lib.channels.wo.euronews',
        'available_languages': ['FR', 'EN', 'AR', 'DE', 'IT', 'ES', 'PT', 'RU', 'TR', 'FA', 'GR', 'HU']
    },
    'arte': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/arte.png',
        'fanart': 'channels/wo/arte_fanart.jpg',
        'module': 'resources.lib.channels.wo.arte',
        'available_languages': ['FR', 'DE'],
        'xmltv_ids': {'fr': 'C111.api.telerama.fr'},
        'm3u_groups': {'fr': 'France TNT'},
        'm3u_orders': {'fr': 7}
    },
    'arirang': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/arirang.png',
        'fanart': 'channels/wo/arirang_fanart.jpg',
        'module': 'resources.lib.channels.wo.arirang'
    },
    'afriquemedia': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/afriquemedia.png',
        'fanart': 'channels/wo/afriquemedia_fanart.jpg',
        'module': 'resources.lib.channels.wo.afriquemedia'
    },
    'dw': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/dw.png',
        'fanart': 'channels/wo/dw_fanart.jpg',
        'module': 'resources.lib.channels.wo.dw',
        'available_languages': ['EN', 'AR', 'ES', 'DE']
    },
    'icirdi': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/icirdi.png',
        'fanart': 'channels/wo/icirdi_fanart.jpg',
        'module': 'resources.lib.channels.wo.icirdi'
    },
    'bvn': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/bvn.png',
        'fanart': 'channels/wo/bvn_fanart.jpg',
        'module': 'resources.lib.channels.wo.bvn'
    },
    'france24': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/france24.png',
        'fanart': 'channels/wo/france24_fanart.jpg',
        'module': 'resources.lib.channels.wo.france24',
        'available_languages': ['FR', 'EN', 'AR', 'ES']
    },
    'qvc': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/qvc.png',
        'fanart': 'channels/wo/qvc_fanart.jpg',
        'module': 'resources.lib.channels.wo.qvc',
        'available_languages': ['JP', 'DE', 'IT', 'UK', 'US']
    },
    'nhkworld': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/nhkworld.png',
        'fanart': 'channels/wo/nhkworld_fanart.jpg',
        'module': 'resources.lib.channels.wo.nhkworld',
        'available_languages': ['Outside Japan', 'In Japan']
    },
    'icitelevision': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/icitelevision.png',
        'fanart': 'channels/wo/icitelevision_fanart.jpg',
        'module': 'resources.lib.channels.wo.icitelevision'
    },
    'channelnewsasia': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/channelnewsasia.png',
        'fanart': 'channels/wo/channelnewsasia_fanart.jpg',
        'module': 'resources.lib.channels.wo.channelnewsasia'
    },
    'cgtn': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/cgtn.png',
        'fanart': 'channels/wo/cgtn_fanart.jpg',
        'module': 'resources.lib.channels.wo.cgtn',
        'available_languages': ['FR', 'EN', 'AR', 'ES', 'RU']
    },
    'cgtndocumentary': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/cgtndocumentary.png',
        'fanart': 'channels/wo/cgtndocumentary_fanart.jpg',
        'module': 'resources.lib.channels.wo.cgtn'
    },
    'paramountchannel': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/paramountchannel.png',
        'fanart': 'channels/wo/paramountchannel_fanart.jpg',
        'module': 'resources.lib.channels.wo.paramountchannel',
        'available_languages': ['ES', 'IT']
    },
    'rt': {
        'callback': 'live_bridge',
        'thumb': 'channels/wo/rt.png',
        'fanart': 'channels/wo/rt_fanart.jpg',
        'module': 'resources.lib.channels.wo.rt',
        'available_languages': ['FR', 'EN', 'AR', 'ES']
    }
}

JP_LIVE = {
    'japanetshoppingdx': {
        'callback': 'live_bridge',
        'thumb': 'channels/jp/japanetshoppingdx.png',
        'fanart': 'channels/jp/japanetshoppingdx_fanart.jpg',
        'module': 'resources.lib.channels.jp.japanetshoppingdx'
    },
    'ntvnews24': {
        'callback': 'live_bridge',
        'thumb': 'channels/jp/ntvnews24.png',
        'fanart': 'channels/jp/ntvnews24_fanart.jpg',
        'module': 'resources.lib.channels.jp.ntvnews24'
    }
}

UK_LIVE = {
    'blaze': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/blaze.png',
        'fanart': 'channels/uk/blaze_fanart.jpg',
        'module': 'resources.lib.channels.uk.blaze'
    },
    'skynews': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/skynews.png',
        'fanart': 'channels/uk/skynews_fanart.jpg',
        'module': 'resources.lib.channels.uk.sky'
    },
    'stv': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/stv.png',
        'fanart': 'channels/uk/stv_fanart.jpg',
        'module': 'resources.lib.channels.uk.stv'
    },
    'kerrang': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/kerrang.png',
        'fanart': 'channels/uk/kerrang_fanart.jpg',
        'module': 'resources.lib.channels.uk.boxplus'
    },
    'magic': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/magic.png',
        'fanart': 'channels/uk/magic_fanart.jpg',
        'module': 'resources.lib.channels.uk.boxplus'
    },
    'kiss': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/kiss.png',
        'fanart': 'channels/uk/kiss_fanart.jpg',
        'module': 'resources.lib.channels.uk.boxplus'
    },
    'the-box': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/thebox.png',
        'fanart': 'channels/uk/thebox_fanart.jpg',
        'module': 'resources.lib.channels.uk.boxplus'
    },
    'box-upfront': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/boxupfront.png',
        'fanart': 'channels/uk/boxupfront_fanart.jpg',
        'module': 'resources.lib.channels.uk.boxplus'
    },
    'box-hits': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/boxhits.png',
        'fanart': 'channels/uk/boxhits_fanart.jpg',
        'module': 'resources.lib.channels.uk.boxplus'
    },
    'questtv': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/questtv.png',
        'fanart': 'channels/uk/questtv_fanart.jpg',
        'module': 'resources.lib.channels.uk.questod'
    },
    'questred': {
        'callback': 'live_bridge',
        'thumb': 'channels/uk/questred.png',
        'fanart': 'channels/uk/questred_fanart.jpg',
        'module': 'resources.lib.channels.uk.questod'
    }
}

BE_LIVE = {
    'bx1': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/bx1.png',
        'fanart': 'channels/be/bx1_fanart.jpg',
        'module': 'resources.lib.channels.be.bx1',
        'm3u_group': 'Belgique fr'
    },
    'nrjhitstvbe': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/nrjhitstvbe.png',
        'fanart': 'channels/be/nrjhitstvbe_fanart.jpg',
        'module': 'resources.lib.channels.be.nrjhitstvbe',
        'm3u_group': 'Belgique fr'
    },
    'auvio': {
        'callback': 'multi_live_bridge',
        'thumb': 'channels/be/auvio.png',
        'fanart': 'channels/be/auvio_fanart.jpg',
        'module': 'resources.lib.channels.be.rtbf'
    },
    'rtc': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/rtc.png',
        'fanart': 'channels/be/rtc_fanart.jpg',
        'module': 'resources.lib.channels.be.rtc',
        'm3u_group': 'Belgique fr'
    },
    'telemb': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/telemb.png',
        'fanart': 'channels/be/telemb_fanart.jpg',
        'module': 'resources.lib.channels.be.telemb',
        'm3u_group': 'Belgique fr'
    },
    'tvlux': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/tvlux.png',
        'fanart': 'channels/be/tvlux_fanart.jpg',
        'module': 'resources.lib.channels.be.tvlux',
        'm3u_group': 'Belgique fr'
    },
    'een': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/een.png',
        'fanart': 'channels/be/een_fanart.jpg',
        'module': 'resources.lib.channels.be.vrt',
        'xmltv_id': 'C23.api.telerama.fr',
        'm3u_group': 'België nl'
    },
    'canvas': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/canvas.png',
        'fanart': 'channels/be/canvas_fanart.jpg',
        'module': 'resources.lib.channels.be.vrt',
        'm3u_group': 'België nl'
    },
    'ketnet': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/ketnet.png',
        'fanart': 'channels/be/ketnet_fanart.jpg',
        'module': 'resources.lib.channels.be.vrt',
        'xmltv_id': 'C1280.api.telerama.fr',
        'm3u_group': 'België nl'
    },
    'tvcom': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/tvcom.png',
        'fanart': 'channels/be/tvcom_fanart.jpg',
        'module': 'resources.lib.channels.be.tvcom',
        'm3u_group': 'Belgique fr'
    },
    'rtl_tvi': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/rtltvi.png',
        'fanart': 'channels/be/rtltvi_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'xmltv_id': 'C168.api.telerama.fr',
        'm3u_group': 'Belgique fr'
    },
    'plug_rtl': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/plugrtl.png',
        'fanart': 'channels/be/plugrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'xmltv_id': 'C377.api.telerama.fr',
        'm3u_group': 'Belgique fr'
    },
    'club_rtl': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/clubrtl.png',
        'fanart': 'channels/be/clubrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'xmltv_id': 'C50.api.telerama.fr',
        'm3u_group': 'Belgique fr'
    },
    'rtl_info': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/rtlinfo.png',
        'fanart': 'channels/be/rtlinfo_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'm3u_group': 'Belgique fr'
    },
    'bel_rtl': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/belrtl.png',
        'fanart': 'channels/be/belrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'm3u_group': 'Belgique fr'
    },
    'contact': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/contact.png',
        'fanart': 'channels/be/contact_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'm3u_group': 'Belgique fr Radio'
    },
    'rtl_sport': {
        'callback': 'live_bridge',
        'thumb': 'channels/be/rtlsport.png',
        'fanart': 'channels/be/rtlsport_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'm3u_group': 'Belgique fr'
    }
}

CA_LIVE = {
    'ntvca': {
        'callback': 'live_bridge',
        'thumb': 'channels/ca/ntvca.png',
        'fanart': 'channels/ca/ntvca_fanart.jpg',
        'module': 'resources.lib.channels.ca.ntvca'
    },
    'tva': {
        'callback': 'live_bridge',
        'thumb': 'channels/ca/tva.png',
        'fanart': 'channels/ca/tva_fanart.jpg',
        'module': 'resources.lib.channels.ca.tva'
    },
    'telequebec': {
        'callback': 'live_bridge',
        'thumb': 'channels/ca/telequebec.png',
        'fanart': 'channels/ca/telequebec_fanart.jpg',
        'module': 'resources.lib.channels.ca.telequebec'
    },
    'icitele': {
        'callback': 'live_bridge',
        'thumb': 'channels/ca/icitele.png',
        'fanart': 'channels/ca/icitele_fanart.jpg',
        'module': 'resources.lib.channels.ca.icitele'
    },
    'telemag': {
        'callback': 'live_bridge',
        'thumb': 'channels/ca/telemag.png',
        'fanart': 'channels/ca/telemag_fanart.jpg',
        'module': 'resources.lib.channels.ca.telemag'
    }
}

CH_LIVE = {
    'rtsun': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rtsun.png',
        'fanart': 'channels/ch/rtsun_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rtsdeux': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rtsdeux.png',
        'fanart': 'channels/ch/rtsdeux_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rtsinfo': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rtsinfo.png',
        'fanart': 'channels/ch/rtsinfo_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rtscouleur3': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rtscouleur3.png',
        'fanart': 'channels/ch/rtscouleur3_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rsila1': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rsila1.png',
        'fanart': 'channels/ch/rsila1_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rsila2': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rsila2.png',
        'fanart': 'channels/ch/rsila2_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'srf1': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/srf1.png',
        'fanart': 'channels/ch/srf1_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'srfinfo': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/srfinfo.png',
        'fanart': 'channels/ch/srfinfo_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'srfzwei': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/srfzwei.png',
        'fanart': 'channels/ch/srfzwei_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rtraufsrf1': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rtraufsrf1.png',
        'fanart': 'channels/ch/rtraufsrf1_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rtraufsrfinfo': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rtraufsrfinfo.png',
        'fanart': 'channels/ch/rtraufsrfinfo_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rtraufsrf2': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rtraufsrf2.png',
        'fanart': 'channels/ch/rtraufsrf2_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rougetv': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/rougetv.png',
        'fanart': 'channels/ch/rougetv_fanart.jpg',
        'module': 'resources.lib.channels.ch.rougetv'
    },
    'teleticino': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/teleticino.png',
        'fanart': 'channels/ch/teleticino_fanart.jpg',
        'module': 'resources.lib.channels.ch.teleticino'
    },
    'lemanbleu': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/lemanbleu.png',
        'fanart': 'channels/ch/lemanbleu_fanart.jpg',
        'module': 'resources.lib.channels.ch.lemanbleu'
    },
    'tvm3': {
        'callback': 'live_bridge',
        'thumb': 'channels/ch/tvm3.png',
        'fanart': 'channels/ch/tvm3_fanart.jpg',
        'module': 'resources.lib.channels.ch.tvm3'
    }
}

US_LIVE = {
    'pbskids': {
        'callback': 'live_bridge',
        'thumb': 'channels/us/pbskids.png',
        'fanart': 'channels/us/pbskids_fanart.jpg',
        'module': 'resources.lib.channels.us.pbskids'
    },
    'tbd': {
        'callback': 'live_bridge',
        'thumb': 'channels/us/tbd.png',
        'fanart': 'channels/us/tbd_fanart.jpg',
        'module': 'resources.lib.channels.us.tbd'
    },
    'cbsnews': {
        'callback': 'live_bridge',
        'thumb': 'channels/us/cbsnews.png',
        'fanart': 'channels/us/cbsnews_fanart.jpg',
        'module': 'resources.lib.channels.us.cbsnews'
    },
    'abcnews': {
        'callback': 'live_bridge',
        'thumb': 'channels/us/abcnews.png',
        'fanart': 'channels/us/abcnews_fanart.jpg',
        'module': 'resources.lib.channels.us.abcnews'
    }
}

IT_LIVE = {
    'la7': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/la7.png',
        'fanart': 'channels/it/la7_fanart.jpg',
        'module': 'resources.lib.channels.it.la7'
    },
    'rainews24': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/rainews24.png',
        'fanart': 'channels/it/rainews24_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'rai1': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/rai1.png',
        'fanart': 'channels/it/rai1_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'rai2': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/rai2.png',
        'fanart': 'channels/it/rai2_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'rai3': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/rai3.png',
        'fanart': 'channels/it/rai3_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'rai4': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/rai4.png',
        'fanart': 'channels/it/rai4_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'rai5': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/rai5.png',
        'fanart': 'channels/it/rai5_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'raisportpiuhd': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/raisportpiuhd.png',
        'fanart': 'channels/it/raisportpiuhd_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'raimovie': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/raimovie.png',
        'fanart': 'channels/it/raimovie_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'raipremium': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/raipremium.png',
        'fanart': 'channels/it/raipremium_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'raiyoyo': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/raiyoyo.png',
        'fanart': 'channels/it/raiyoyo_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'raigulp': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/raigulp.png',
        'fanart': 'channels/it/raigulp_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'raistoria': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/raistoria.png',
        'fanart': 'channels/it/raistoria_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    },
    'raiscuola': {
        'callback': 'live_bridge',
        'thumb': 'channels/it/raiscuola.png',
        'fanart': 'channels/it/raiscuola_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    }
}

NL_LIVE = {
    'npo-1': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/npo1.png',
        'fanart': 'channels/nl/npo1_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'npo-2': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/npo2.png',
        'fanart': 'channels/nl/npo2_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'npo-zapp': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/npozapp.png',
        'fanart': 'channels/nl/npozapp_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'npo-1-extra': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/npo1extra.png',
        'fanart': 'channels/nl/npo1extra_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'npo-2-extra': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/npo2extra.png',
        'fanart': 'channels/nl/npo2extra_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'npo-zappelin-extra': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/npozappelinextra.png',
        'fanart': 'channels/nl/npozappelinextra_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'npo-nieuws': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/nponieuws.png',
        'fanart': 'channels/nl/nponieuws_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'npo-politiek': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/npopolitiek.png',
        'fanart': 'channels/nl/npopolitiek_fanart.jpg',
        'module': 'resources.lib.channels.nl.npo'
    },
    'at5': {
        'callback': 'live_bridge',
        'thumb': 'channels/nl/at5.png',
        'fanart': 'channels/nl/at5_fanart.jpg',
        'module': 'resources.lib.channels.nl.at5'
    }
}

FR_REPLAY = {
    'tf1': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tf1.png',
        'fanart': 'channels/fr/tf1_fanart.png',
        'module': 'resources.lib.channels.fr.mytf1'
    },
    'tmc': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tmc.png',
        'fanart': 'channels/fr/tmc_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1'
    },
    'tf1-series-films': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tf1seriesfilms.png',
        'fanart': 'channels/fr/tf1seriesfilms_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1'
    },
    'tfx': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tfx.png',
        'fanart': 'channels/fr/tfx_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1'
    },
    'tfou': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tfou.png',
        'fanart': 'channels/fr/tfou_fanart.jpg',
        'module': 'resources.lib.channels.fr.mytf1'
    },
    'm6': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/m6.png',
        'fanart': 'channels/fr/m6_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play'
    },
    'w9': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/w9.png',
        'fanart': 'channels/fr/w9_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play'
    },
    '6ter': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/6ter.png',
        'fanart': 'channels/fr/6ter_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play'
    },
    'rtl2': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/rtl2.png',
        'fanart': 'channels/fr/rtl2_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play'
    },
    'fun_radio': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/funradio.png',
        'fanart': 'channels/fr/funradio_fanart.jpg',
        'module': 'resources.lib.channels.fr.6play'
    },
    'lci': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/lci.png',
        'fanart': 'channels/fr/lci_fanart.jpg',
        'module': 'resources.lib.channels.fr.lci'
    },
    'gulli': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/gulli.png',
        'fanart': 'channels/fr/gulli_fanart.jpg',
        'module': 'resources.lib.channels.fr.gulli'
    },
    'canalplus': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/canalplus.png',
        'fanart': 'channels/fr/canalplus_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'c8': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/c8.png',
        'fanart': 'channels/fr/c8_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'cstar': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/cstar.png',
        'fanart': 'channels/fr/cstar_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'seasons': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/seasons.png',
        'fanart': 'channels/fr/seasons_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'comedie': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/comedie.png',
        'fanart': 'channels/fr/comedie_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'les-chaines-planete': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/leschainesplanete.png',
        'fanart': 'channels/fr/leschainesplanete_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'golfplus': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/golfplus.png',
        'fanart': 'channels/fr/golfplus_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'cineplus': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/cineplus.png',
        'fanart': 'channels/fr/cineplus_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'infosportplus': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/infosportplus.png',
        'fanart': 'channels/fr/infosportplus_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'polar-plus': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/polarplus.png',
        'fanart': 'channels/fr/polarplus_fanart.jpg',
        'module': 'resources.lib.channels.fr.mycanal'
    },
    'france-2': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/france2.png',
        'fanart': 'channels/fr/france2_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv'
    },
    'france-3': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/france3.png',
        'fanart': 'channels/fr/france3_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv'
    },
    'france-4': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/france4.png',
        'fanart': 'channels/fr/france4_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv'
    },
    'france-5': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/france5.png',
        'fanart': 'channels/fr/france5_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv'
    },
    'france-o': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/franceo.png',
        'fanart': 'channels/fr/franceo_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv'
    },
    'lequipe': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/lequipe.png',
        'fanart': 'channels/fr/lequipe_fanart.jpg',
        'module': 'resources.lib.channels.fr.lequipe'
    },
    'cnews': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/cnews.png',
        'fanart': 'channels/fr/cnews_fanart.jpg',
        'module': 'resources.lib.channels.fr.cnews'
    },
    'rmcdecouverte': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/rmcdecouverte.png',
        'fanart': 'channels/fr/rmcdecouverte_fanart.jpg',
        'module': 'resources.lib.channels.fr.rmcdecouverte'
    },
    'rmcstory': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/rmcstory.png',
        'fanart': 'channels/fr/rmcstory_fanart.jpg',
        'module': 'resources.lib.channels.fr.rmcstory'
    },
    'nrj12': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/nrj12.png',
        'fanart': 'channels/fr/nrj12_fanart.jpg',
        'module': 'resources.lib.channels.fr.nrj'
    },
    'cherie25': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/cherie25.png',
        'fanart': 'channels/fr/cherie25_fanart.jpg',
        'module': 'resources.lib.channels.fr.nrj'
    },
    'lachainemeteo': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/lachainemeteo.png',
        'fanart': 'channels/fr/lachainemeteo_fanart.jpg',
        'module': 'resources.lib.channels.fr.lachainemeteo'
    },
    'histoire': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/histoire.png',
        'fanart': 'channels/fr/histoire_fanart.jpg',
        'module': 'resources.lib.channels.fr.tf1thematiques'
    },
    'tvbreizh': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tvbreizh.png',
        'fanart': 'channels/fr/tvbreizh_fanart.jpg',
        'module': 'resources.lib.channels.fr.tf1thematiques'
    },
    'ushuaiatv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/ushuaiatv.png',
        'fanart': 'channels/fr/ushuaiatv_fanart.jpg',
        'module': 'resources.lib.channels.fr.tf1thematiques'
    },
    'slash': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/slash.png',
        'fanart': 'channels/fr/slash_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetv'
    },
    'bfmparis': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/bfmparis.png',
        'fanart': 'channels/fr/bfmparis_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmparis'
    },
    'bfmtv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/bfmtv.png',
        'fanart': 'channels/fr/bfmtv_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmtv'
    },
    'bfmbusiness': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/bfmbusiness.png',
        'fanart': 'channels/fr/bfmbusiness_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmtv'
    },
    'rmc': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/rmc.png',
        'fanart': 'channels/fr/rmc_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmtv'
    },
    '01net': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/01net.png',
        'fanart': 'channels/fr/01net_fanart.jpg',
        'module': 'resources.lib.channels.fr.bfmtv'
    },
    'gong': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/gong.png',
        'fanart': 'channels/fr/gong_fanart.jpg',
        'module': 'resources.lib.channels.fr.gong'
    },
    'la_1ere': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/la1ere.png',
        'fanart': 'channels/fr/la1ere_fanart.jpg',
        'module': 'resources.lib.channels.fr.la_1ere'
    },
    'kto': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/kto.png',
        'fanart': 'channels/fr/kto_fanart.jpg',
        'module': 'resources.lib.channels.fr.kto'
    },
    'ouatchtv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/ouatchtv.png',
        'fanart': 'channels/fr/ouatchtv_fanart.jpg',
        'module': 'resources.lib.channels.fr.ouatchtv'
    },
    'onzeo': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/onzeo.png',
        'fanart': 'channels/fr/onzeo_fanart.jpg',
        'module': 'resources.lib.channels.fr.onzeo'
    },
    'publicsenat': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/publicsenat.png',
        'fanart': 'channels/fr/publicsenat_fanart.jpg',
        'module': 'resources.lib.channels.fr.publicsenat'
    },
    'lcp': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/lcp.png',
        'fanart': 'channels/fr/lcp_fanart.jpg',
        'module': 'resources.lib.channels.fr.lcp'
    },
    'gameone': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/gameone.png',
        'fanart': 'channels/fr/gameone_fanart.jpg',
        'module': 'resources.lib.channels.fr.gameone'
    },
    'francetvsport': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/francetvsport.png',
        'fanart': 'channels/fr/francetvsport_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetvsport'
    },
    'franceinfo': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/franceinfo.png',
        'fanart': 'channels/fr/franceinfo_fanart.jpg',
        'module': 'resources.lib.channels.fr.franceinfo'
    },
    'france3regions': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/france3regions.png',
        'fanart': 'channels/fr/france3regions_fanart.jpg',
        'module': 'resources.lib.channels.fr.france3regions'
    },
    'culturebox': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/culturebox.png',
        'fanart': 'channels/fr/culturebox_fanart.jpg',
        'module': 'resources.lib.channels.fr.culturebox'
    },
    'francetveducation': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/francetveducation.png',
        'fanart': 'channels/fr/francetveducation_fanart.jpg',
        'module': 'resources.lib.channels.fr.francetveducation'
    },
    'irl': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/irl.png',
        'fanart': 'channels/fr/irl_fanart.jpg',
        'module': 'resources.lib.channels.fr.nouvellesecritures'
    },
    'studio-4': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/studio4.png',
        'fanart': 'channels/fr/studio4_fanart.jpg',
        'module': 'resources.lib.channels.fr.nouvellesecritures'
    },
    'j_one': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/jone.png',
        'fanart': 'channels/fr/jone_fanart.jpg',
        'module': 'resources.lib.channels.fr.j_one'
    },
    'jack': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/jack.png',
        'fanart': 'channels/fr/jack_fanart.jpg',
        'module': 'resources.lib.channels.fr.jack'
    },
    'antennereunion': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/antennereunion.png',
        'fanart': 'channels/fr/antennereunion_fanart.jpg',
        'module': 'resources.lib.channels.fr.antennereunion'
    },
    'caledonia': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/caledonia.png',
        'fanart': 'channels/fr/caledonia_fanart.jpg',
        'module': 'resources.lib.channels.fr.caledonia'
    },
    'tebeo': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tebeo.png',
        'fanart': 'channels/fr/tebeo_fanart.jpg',
        'module': 'resources.lib.channels.fr.tebeo'
    },
    'via93': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/via93.png',
        'fanart': 'channels/fr/via93_fanart.jpg',
        'module': 'resources.lib.channels.fr.via'
    },
    'tl7': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tl7.png',
        'fanart': 'channels/fr/tl7_fanart.jpg',
        'module': 'resources.lib.channels.fr.tl7'
    },
    'mblivetv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/mblivetv.png',
        'fanart': 'channels/fr/mblivetv_fanart.jpg',
        'module': 'resources.lib.channels.fr.mblivetv'
    },
    'tv8montblanc': {
        'callback': 'replay_bridge',
        'thumb': 'channels/fr/tv8montblanc.png',
        'fanart': 'channels/fr/tv8montblanc_fanart.jpg',
        'module': 'resources.lib.channels.fr.tv8montblanc'
    }
}


UK_REPLAY = {
    'questod': {
        'callback': 'replay_bridge',
        'thumb': 'channels/uk/questod.png',
        'fanart': 'channels/uk/questod_fanart.jpg',
        'module': 'resources.lib.channels.uk.questod'
    },
    'blaze': {
        'callback': 'replay_bridge',
        'thumb': 'channels/uk/blaze.png',
        'fanart': 'channels/uk/blaze_fanart.jpg',
        'module': 'resources.lib.channels.uk.blaze'
    },
    'skynews': {
        'callback': 'replay_bridge',
        'thumb': 'channels/uk/skynews.png',
        'fanart': 'channels/uk/skynews_fanart.jpg',
        'module': 'resources.lib.channels.uk.sky'
    },
    'skysports': {
        'callback': 'replay_bridge',
        'thumb': 'channels/uk/skysports.png',
        'fanart': 'channels/uk/skysports_fanart.jpg',
        'module': 'resources.lib.channels.uk.sky'
    },
    'stv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/uk/stv.png',
        'fanart': 'channels/uk/stv_fanart.jpg',
        'module': 'resources.lib.channels.uk.stv'
    },
    'uktvplay': {
        'callback': 'replay_bridge',
        'thumb': 'channels/uk/uktvplay.png',
        'fanart': 'channels/uk/uktvplay_fanart.jpg',
        'module': 'resources.lib.channels.uk.uktvplay'
    }
}


BE_REPLAY = {
    'rtl_tvi': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtltvi.png',
        'fanart': 'channels/be/rtltvi_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'plug_rtl': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/plugrtl.png',
        'fanart': 'channels/be/plugrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'club_rtl': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/clubrtl.png',
        'fanart': 'channels/be/clubrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'rtl_info': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtlinfo.png',
        'fanart': 'channels/be/rtlinfo_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'bel_rtl': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/belrtl.png',
        'fanart': 'channels/be/belrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'contact': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/contact.png',
        'fanart': 'channels/be/contact_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'rtl_sport': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtlsport.png',
        'fanart': 'channels/be/rtlsport_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'brf': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/brf.png',
        'fanart': 'channels/be/brf_fanart.jpg',
        'module': 'resources.lib.channels.be.brf'
    },
    'bx1': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/bx1.png',
        'fanart': 'channels/be/bx1_fanart.jpg',
        'module': 'resources.lib.channels.be.bx1'
    },
    'nrjhitstvbe': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/nrjhitstvbe.png',
        'fanart': 'channels/be/nrjhitstvbe_fanart.jpg',
        'module': 'resources.lib.channels.be.nrjhitstvbe'
    },
    'auvio': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/auvio.png',
        'fanart': 'channels/be/auvio_fanart.jpg',
        'module': 'resources.lib.channels.be.rtbf'
    },
    'rtc': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtc.png',
        'fanart': 'channels/be/rtc_fanart.jpg',
        'module': 'resources.lib.channels.be.rtc'
    },
    'telemb': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/telemb.png',
        'fanart': 'channels/be/telemb_fanart.jpg',
        'module': 'resources.lib.channels.be.telemb'
    },
    'tvlux': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/tvlux.png',
        'fanart': 'channels/be/tvlux_fanart.jpg',
        'module': 'resources.lib.channels.be.tvlux'
    },
    'vrt': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/vrt.png',
        'fanart': 'channels/be/vrt_fanart.jpg',
        'module': 'resources.lib.channels.be.vrt'
    },
    'tvcom': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/tvcom.png',
        'fanart': 'channels/be/tvcom_fanart.jpg',
        'module': 'resources.lib.channels.be.tvcom'
    }
}

WO_REPLAY = {
    'tv5mondeafrique': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/tv5mondeafrique.png',
        'fanart': 'channels/wo/tv5mondeafrique_fanart.jpg',
        'module': 'resources.lib.channels.wo.tv5mondeafrique'
    },
    'tivi5monde': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/tivi5monde.png',
        'fanart': 'channels/wo/tivi5monde_fanart.jpg',
        'module': 'resources.lib.channels.wo.tivi5monde'
    },
    'tv5monde': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/tv5monde.png',
        'fanart': 'channels/wo/tv5monde_fanart.jpg',
        'module': 'resources.lib.channels.wo.tv5monde'
    },
    'arte': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/arte.png',
        'fanart': 'channels/wo/arte_fanart.jpg',
        'module': 'resources.lib.channels.wo.arte'
    },
    'arirang': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/arirang.png',
        'fanart': 'channels/wo/arirang_fanart.jpg',
        'module': 'resources.lib.channels.wo.arirang'
    },
    'afriquemedia': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/afriquemedia.png',
        'fanart': 'channels/wo/afriquemedia_fanart.jpg',
        'module': 'resources.lib.channels.wo.afriquemedia'
    },
    'beinsports': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/beinsports.png',
        'fanart': 'channels/wo/beinsports_fanart.jpg',
        'module': 'resources.lib.channels.wo.beinsports'
    },
    'bvn': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/bvn.png',
        'fanart': 'channels/wo/bvn_fanart.jpg',
        'module': 'resources.lib.channels.wo.bvn'
    },
    'mtv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/mtv.png',
        'fanart': 'channels/wo/mtv_fanart.jpg',
        'module': 'resources.lib.channels.wo.mtv'
    },
    'nhkworld': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/nhkworld.png',
        'fanart': 'channels/wo/nhkworld_fanart.jpg',
        'module': 'resources.lib.channels.wo.nhkworld'
    },
    'channelnewsasia': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/channelnewsasia.png',
        'fanart': 'channels/wo/channelnewsasia_fanart.jpg',
        'module': 'resources.lib.channels.wo.channelnewsasia'
    },
    'france24': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/france24.png',
        'fanart': 'channels/wo/france24_fanart.jpg',
        'module': 'resources.lib.channels.wo.france24'
    },
    'rt': {
        'callback': 'replay_bridge',
        'thumb': 'channels/wo/rt.png',
        'fanart': 'channels/wo/rt_fanart.jpg',
        'module': 'resources.lib.channels.wo.rt',
        'available_languages': ['FR', 'EN']
    }
}

JP_REPLAY = {
    'tbsnews': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/tbsnews.png',
        'fanart': 'channels/jp/tbsnews_fanart.jpg',
        'module': 'resources.lib.channels.jp.tbsnews'
    },
    'ntv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/ntv.png',
        'fanart': 'channels/jp/ntv_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    },
    'ex': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/ex.png',
        'fanart': 'channels/jp/ex_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    },
    'tbs': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/tbs.png',
        'fanart': 'channels/jp/tbs_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    },
    'tx': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/tx.png',
        'fanart': 'channels/jp/tx_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    },
    'mbs': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/mbs.png',
        'fanart': 'channels/jp/mbs_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    },
    'abc': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/abc.png',
        'fanart': 'channels/jp/abc_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    },
    'ytv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/ytv.png',
        'fanart': 'channels/jp/ytv_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    },
    'nhknews': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/nhknews.png',
        'fanart': 'channels/jp/nhknews_fanart.jpg',
        'module': 'resources.lib.channels.jp.nhknews'
    },
    'nhklifestyle': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/nhklifestyle.png',
        'fanart': 'channels/jp/nhklifestyle_fanart.jpg',
        'module': 'resources.lib.channels.jp.nhklifestyle'
    },
    'ktv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/jp/ktv.png',
        'fanart': 'channels/jp/ktv_fanart.jpg',
        'module': 'resources.lib.channels.jp.tver'
    }
}

CH_REPLAY = {
    'rts': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/rts.png',
        'fanart': 'channels/ch/rts_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rsi': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/rsi.png',
        'fanart': 'channels/ch/rsi_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'srf': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/srf.png',
        'fanart': 'channels/ch/srf_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'rtr': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/rtr.png',
        'fanart': 'channels/ch/rtr_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'swissinfo': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/swissinfo.png',
        'fanart': 'channels/ch/swissinfo_fanart.jpg',
        'module': 'resources.lib.channels.ch.srgssr'
    },
    'tvm3': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/tvm3.png',
        'fanart': 'channels/ch/tvm3_fanart.jpg',
        'module': 'resources.lib.channels.ch.tvm3'
    },
    'becurioustv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/becurioustv.png',
        'fanart': 'channels/ch/becurioustv_fanart.jpg',
        'module': 'resources.lib.channels.ch.becurioustv'
    },
    'lemanbleu': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ch/lemanbleu.png',
        'fanart': 'channels/ch/lemanbleu_fanart.jpg',
        'module': 'resources.lib.channels.ch.lemanbleu'
    }
}

CA_REPLAY = {
    'tva': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ca/tva.png',
        'fanart': 'channels/ca/tva_fanart.jpg',
        'module': 'resources.lib.channels.ca.tva'
    },
    'tv5': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ca/tv5.png',
        'fanart': 'channels/ca/tv5_fanart.jpg',
        'module': 'resources.lib.channels.ca.tv5'
    },
    'unis': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ca/unis.png',
        'fanart': 'channels/ca/unis_fanart.jpg',
        'module': 'resources.lib.channels.ca.tv5'
    },
    'telequebec': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ca/telequebec.png',
        'fanart': 'channels/ca/telequebec_fanart.jpg',
        'module': 'resources.lib.channels.ca.telequebec'
    },
    'icitoutv': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ca/icitoutv.png',
        'fanart': 'channels/ca/icitoutv_fanart.jpg',
        'module': 'resources.lib.channels.ca.icitoutv'
    },
    'icitele': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ca/icitele.png',
        'fanart': 'channels/ca/icitele_fanart.jpg',
        'module': 'resources.lib.channels.ca.icitele'
    },
    'telemag': {
        'callback': 'replay_bridge',
        'thumb': 'channels/ca/telemag.png',
        'fanart': 'channels/ca/telemag_fanart.jpg',
        'module': 'resources.lib.channels.ca.telemag'
    }
}

US_REPLAY = {
    'tbd': {
        'callback': 'replay_bridge',
        'thumb': 'channels/us/tbd.png',
        'fanart': 'channels/us/tbd_fanart.jpg',
        'module': 'resources.lib.channels.us.tbd'
    },
    'nycmedia': {
        'callback': 'replay_bridge',
        'thumb': 'channels/us/nycmedia.png',
        'fanart': 'channels/us/nycmedia_fanart.jpg',
        'module': 'resources.lib.channels.us.nycmedia'
    },
    'abcnews': {
        'callback': 'replay_bridge',
        'thumb': 'channels/us/abcnews.png',
        'fanart': 'channels/us/abcnews_fanart.jpg',
        'module': 'resources.lib.channels.us.abcnews'
    }
}

ES_REPLAY = {
}

IT_REPLAY = {
    'la7': {
        'callback': 'replay_bridge',
        'thumb': 'channels/it/la7.png',
        'fanart': 'channels/it/la7_fanart.jpg',
        'module': 'resources.lib.channels.it.la7'
    },
    'la7d': {
        'callback': 'replay_bridge',
        'thumb': 'channels/it/la7d.png',
        'fanart': 'channels/it/la7d_fanart.jpg',
        'module': 'resources.lib.channels.it.la7'
    },
    'raiplay': {
        'callback': 'replay_bridge',
        'thumb': 'channels/it/raiplay.png',
        'fanart': 'channels/it/raiplay_fanart.jpg',
        'module': 'resources.lib.channels.it.raiplay'
    }
}

TN_REPLAY = {
    'nessma': {
        'callback': 'replay_bridge',
        'thumb': 'channels/tn/nessma.png',
        'fanart': 'channels/tn/nessma_fanart.jpg',
        'module': 'resources.lib.channels.tn.nessma'
    }
}

NL_REPLAY = {
    'at5': {
        'callback': 'replay_bridge',
        'thumb': 'channels/nl/at5.png',
        'fanart': 'channels/nl/at5_fanart.jpg',
        'module': 'resources.lib.channels.nl.at5'
    }
}

WEBSITES = {
    'allocine': {
        'callback': 'website_bridge',
        'thumb': 'websites/allocine.png',
        'fanart': 'websites/allocine_fanart.jpg',
        'module': 'resources.lib.websites.allocine'
    },
    'tetesaclaques': {
        'callback': 'website_bridge',
        'thumb': 'websites/tetesaclaques.png',
        'fanart': 'websites/tetesaclaques_fanart.jpg',
        'module': 'resources.lib.websites.tetesaclaques'
    },
    'taratata': {
        'callback': 'website_bridge',
        'thumb': 'websites/taratata.png',
        'fanart': 'websites/taratata_fanart.jpg',
        'module': 'resources.lib.websites.taratata'
    },
    'onf': {
        'callback': 'website_bridge',
        'thumb': 'websites/onf.png',
        'fanart': 'websites/onf_fanart.jpg',
        'module': 'resources.lib.websites.onf'
    },
    'nytimes': {
        'callback': 'website_bridge',
        'thumb': 'websites/nytimes.png',
        'fanart': 'websites/nytimes_fanart.jpg',
        'module': 'resources.lib.websites.nytimes'
    },
    'notrehistoirech': {
        'callback': 'website_bridge',
        'thumb': 'websites/notrehistoirech.png',
        'fanart': 'websites/notrehistoirech_fanart.jpg',
        'module': 'resources.lib.websites.notrehistoirech'
    },
    'noob': {
        'callback': 'website_bridge',
        'thumb': 'websites/noob.png',
        'fanart': 'websites/noob_fanart.jpg',
        'module': 'resources.lib.websites.noob'
    },
    'nfb': {
        'callback': 'website_bridge',
        'thumb': 'websites/nfb.png',
        'fanart': 'websites/nfb_fanart.jpg',
        'module': 'resources.lib.websites.nfb'
    },
    'ina': {
        'callback': 'website_bridge',
        'thumb': 'websites/ina.png',
        'fanart': 'websites/ina_fanart.jpg',
        'module': 'resources.lib.websites.ina'
    },
    'fosdem': {
        'callback': 'website_bridge',
        'thumb': 'websites/fosdem.png',
        'fanart': 'websites/fosdem_fanart.jpg',
        'module': 'resources.lib.websites.fosdem'
    },
    'elle': {
        'callback': 'website_bridge',
        'thumb': 'websites/elle.png',
        'fanart': 'websites/elle_fanart.jpg',
        'module': 'resources.lib.websites.elle'
    },
    'culturepub': {
        'callback': 'website_bridge',
        'thumb': 'websites/culturepub.png',
        'fanart': 'websites/culturepub_fanart.jpg',
        'module': 'resources.lib.websites.culturepub'
    },
    'autoplus': {
        'callback': 'website_bridge',
        'thumb': 'websites/autoplus.png',
        'fanart': 'websites/autoplus_fanart.jpg',
        'module': 'resources.lib.websites.autoplus'
    },
    '30millionsdamis': {
        'callback': 'website_bridge',
        'thumb': 'websites/30millionsdamis.png',
        'fanart': 'websites/30millionsdamis_fanart.jpg',
        'module': 'resources.lib.websites.30millionsdamis'
    },
    'marmiton': {
        'callback': 'website_bridge',
        'thumb': 'websites/marmiton.png',
        'fanart': 'websites/marmiton_fanart.jpg',
        'module': 'resources.lib.websites.marmiton'
    },
    'lesargonautes': {
        'callback': 'website_bridge',
        'thumb': 'websites/lesargonautes.png',
        'fanart': 'websites/lesargonautes_fanart.jpg',
        'module': 'resources.lib.websites.lesargonautes'
    },
    'nationalfff': {
        'callback': 'website_bridge',
        'thumb': 'websites/nationalfff.png',
        'fanart': 'websites/nationalfff_fanart.jpg',
        'module': 'resources.lib.websites.nationalfff'
    }
}
