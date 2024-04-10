# tenenat -> prompt, tags, wordrepresentation
# extractor -> prompt, tags, wordrepresentation
from .tags import general_tags, kid_tags, gkid_tags
from .prompts import general_prompts, kid_prompts, gkid_prompts
from .tags.waminsurance import waminsurance_tags
# Word represenatiations
from .word_representation import kid_wr, gkid_wr
from .word_representation.wamderivati import derivatives_wr


extraction_configurations = {
    'general':{
        'word_representation':{
        },
        'prompt':{
        },
        'tag':{
            'doc_language': general_tags.DocLanguage,
        },            
    },
    # WAMINSURANCE
    'waminsurance':{
        'general':{
            'word_representation':{
                'performance': kid_wr.performance,
                'riy': kid_wr.riy,
                'costi_ingresso': kid_wr.costi_ingresso,
                'costi_gestione': kid_wr.costi_gestione                
            },
            'prompt':{
                'general_info': kid_prompts.general_info,
                'performance': kid_prompts.performance1y,
                'performance_abs': kid_prompts.performance_abs,
                'performance_rhp_2': kid_prompts.performance_rhp_2,
                'target_market': kid_prompts.target_market,
                'riy': kid_prompts.riy,
                'riy_small': kid_prompts.riy_small,
                'riy_rhp_2': kid_prompts.riy_rhp2
            },
            'tag':{
                'general_info': kid_tags.InformazioniBase,
                'is_complex': kid_tags.IsDisclaimerThere,
                'performance': kid_tags.TabellaScenariPerformance,
                'riy': kid_tags.TabellaRiy,
                'riy_small': kid_tags.TabellaRiySmall,
                'riy_rhp_2': kid_tags.TabellaRiyRHP2,
                'costi_ingresso': kid_tags.TabellaCostiIngresso,
                'costi_gestione': kid_tags.TabellaCostiGestione,
            },            
        },
        'kidgovernance':{
            'word_representation':{
            },
            'prompt':{
            },
            'tag':{
                'performance_abs': kid_tags.ScenariPerformanceAbsoluteEuro,
                'performance_rhp_2': kid_tags.ScenariPerformanceRHP2
                }
        },
        'kidcredem':{
            'word_representation':{
            },
            'prompt':{
            },
            'tag':{
                'performance': waminsurance_tags.TabellaScenariPerformanceCredem,
            } 
        },
        'kidmodule':{
            'word_representation':{
            },
            'prompt':{
            },
            'tag':{
            }
        },
        'gkidgovernance':{
            'word_representation':{
                'costi_ingresso': gkid_wr.costi_ingresso_gkid,
                'costi_gestione': gkid_wr.costi_gestione_gkid,
                'riy': gkid_wr.riy_perc_gkid
            },
            'prompt':{
                'general_info': gkid_prompts.general_info_gkid,
                'target_market': gkid_prompts.market_gkid
            },
            'tag':{
                'general_info': gkid_tags.InformazioniBaseGkid
            }
        }
    },
    # WAMDERIVATI
    'wamderivati':{
        'general':{
            'word_representation':{
                'cedola': derivatives_wr.cedola,
                'sottostanti': derivatives_wr.sottostanti,
                'main_info': derivatives_wr.main_info,
                'sottostanti_table': derivatives_wr.sottostanti_table,
                'first_info_bnp': derivatives_wr.first_info_bnp,
                'main_info_bnp': derivatives_wr.main_info_bnp,
                'main_info_bnp2': derivatives_wr.main_info_bnp2,
                'sottostante_bnp': derivatives_wr.sottostante_bnp,
                'allegato_bnp_premio': derivatives_wr.allegato_bnp_premio,
                'allegato_bnp_scadenza': derivatives_wr.allegato_bnp_scadenza
            },
            'prompt':{
            },
            'tag':{
                
            },            
        },
        'complexity':{
            'word_representation':{
            },
            'prompt':{
            },
            'tag':{
                'general_info': ''#waminsurance_tags.InformazioniBaseKidGov
                }
        }
}
}
