# tenenat -> prompt, tags, wordrepresentation
# extractor -> prompt, tags, wordrepresentation
from .tags import general_tags, kid_tags, gkid_tags
from .prompts import general_prompts, kid_prompts, gkid_prompts
from .prompts.wamderivati import demo_prompt, bnpproduction_prompt, rettifichebi_prompt
from .tags.wamderivati import rettifichebi_tags #bnpproduction_tags, 

from .tags.waminsurance import waminsurance_tags, cga, kidmodule_tags

from .tags.wamasset import kidasset_tags
from .prompts.wasasset import wasasset_prompts
from .prompts.waminsurance import kidmodule_prompt
# Word represenatiations
from .word_representation import kid_wr, gkid_wr
from .word_representation.wamderivati import derivatives_wr
from .word_representation.wamasset import wakid_wr
from .tags.wamderivati import demo_tags, production_tags

###########
# ITALIAN #
###########
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
                'performance': kid_prompts.performance,
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
                'general_info': kidmodule_prompt.general_info,
                'performance': kid_prompts.performance,
                'sottostante' : kidmodule_prompt.sottostante
            },
            'tag':{
                'general_info':kidmodule_tags.InformazioniPremio,
                'sottostante':kidmodule_tags.SottostanteInfo,
            }
        },
        'cga':{
            'word_representation':{
            },
            'prompt':{

            },
            'tag':{
                'vita_intera': cga.IsVitaIntera,
                'is_unico': cga.IsUnico,
                'is_premio_ricorrente': cga.IsPremioRicorrente,
                'durata': cga.Durata,
                'premium_type': cga.PremiumType,
                'premium_boundaries': cga.PremiumBoundaries
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
                'performance': kid_wr.performance,
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
                'performance': production_tags.TabellaScenariPerformance,
                'costi_ingresso': kid_tags.TabellaCostiIngresso,
                'costi_gestione': kid_tags.TabellaCostiGestione,

            },            
        },
        'demo':{
            'word_representation':{
            },
            'prompt':{
                'demo_human': demo_prompt.demo_human,
                'demo_system': demo_prompt.demo_system
            },
            'tag':{
                'demo': demo_tags.DemoTag
                }
        },
        'bnp':{
            'word_representation':{
                'sottostante_bnp': derivatives_wr.sottostante_bnp,
            },
            'prompt':{
                'general_info': bnpproduction_prompt.general_info_bnp,
                'first_info_bnp': bnpproduction_prompt.first_info_bnp,
                'main_info_bnp': bnpproduction_prompt.main_info_bnp,
                'allegato_bnp_premio': bnpproduction_prompt.allegato_bnp_premio,
                'allegato_bnp_scadenza': bnpproduction_prompt.allegato_bnp_scadenza,
                'allegati_bnp': bnpproduction_prompt.allegati_bnp
            },
            'tag':{

                'general_info': production_tags.InformazioniBaseBNP,
                'first_info_bnp': production_tags.TabellaFirstInfoBNP,
                'main_info_bnp': production_tags.TabellaMainInfoBNP,
                'allegato_bnp_premio': production_tags.TabellaAllegatoPremioBNP,
                'allegato_bnp_scadenza': production_tags.TabellaAllegatoScadenzaBNP,
                'allegati_bnp': production_tags.TabellaAllegatiBNP,
                'sottostante_bnp': production_tags.TabellaSottostanteBNP,

            }
           #"sottostanti": TabellaSottostanti,
#         "main_info": TabellaMainInfo,
#         "cedola_str": CedolaStr,
#         "general_info_certificati": InformazioniBaseCertificati,
#         "sottostanti_header": TabellaSottostantiHeader,
        },
        'rettifichebi':{
            'word_representation':{
            },
            'prompt':{
                'rettifichebi_human': rettifichebi_prompt.rettifichebi_human,
                'rettifichebi_system': rettifichebi_prompt.rettifichebi_system
            },
            'tag':{
                'rettifichebi': rettifichebi_tags.RettificheBIInfo
                }
        }
        },
    'wamasset':{
        'general':{
                'word_representation':{
                    'performance': kid_wr.performance,
                    'costi_ingresso': kid_wr.costi_ingresso,
                    'costi_gestione': kid_wr.costi_gestione
                },
                'prompt':{
                },
                'tag':{
                }
        },
        'kidasset':{
                'word_representation':{
                        'costi_ingresso': wakid_wr.costi_ingresso,
                        'costi_gestione': wakid_wr.costi_gestione
                },
                'prompt':{
                    'general_info': wasasset_prompts.general_info,
                    'costi_ingresso': wasasset_prompts.costi_ingresso_diritti_fissi,
                    'costi_gestione': wasasset_prompts.costi_gestione_performance,
                    #'class': wasasset_prompts.classe_fondo,
                    'strategy': wasasset_prompts.strategia_fondo
                },
                'tag':{
                    'general_info': kidasset_tags.InformazioniBase,
                    'costi_ingresso': kidasset_tags.TabellaCostiIngressoDirttiFissi,
                    'costi_gestione': kidasset_tags.TabellaCostiGestionePerformance,
                    'picpac': kidasset_tags.PicPac,
                    #'class': kidasset_tags.FundClass
                }
        }
}}



###########
# ENGLISH #
###########
extraction_configurations_eng = {
    'general':{
        'word_representation':{
        },
        'prompt':{
        },
        'tag':{
            'doc_language': general_tags.DocLanguage,
        },            
    },
    'wamasset':{
        'general':{
                'word_representation':{
                },
                'prompt':{
                },
                'tag':{
                }
        },
        'kidasset':{
                'word_representation':{
                        'costi_ingresso': wakid_wr.entry_exit_costs,
                        'costi_gestione': wakid_wr.management_costs
                },
                'prompt':{
                    'general_info': wasasset_prompts.general_info_eng,
                    'costi_ingresso': wasasset_prompts.entry_exit_costs_fixed_rights,
                    'costi_gestione': wasasset_prompts.management_costs_performance,
                    #'class': wasasset_prompts.classe_fondo,
                    'strategy': wasasset_prompts.investment_strategy
                
                },
                'tag':{
                    'general_info': kidasset_tags.BasicInformation,
                    'costi_ingresso': kidasset_tags.TableEntryExitFixedRights,
                    'costi_gestione': kidasset_tags.TableManagementPerformance,
                    #'picpac': kidasset_tags.PicPacEng,
                    #'class': kidasset_tags.FundClass
                }}
}}