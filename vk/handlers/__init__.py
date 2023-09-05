from handlers.menu import menu_router
from handlers.reg.reg_profile import reg_profile_router
from handlers.reg.reg_name import reg_name_router
from handlers.reg.reg_bdate import reg_bdate_router
from handlers.reg.reg_sex import reg_sex_router
from handlers.reg.reg_geo import reg_geo_router
from handlers.reg.reg_photos import reg_photo_router
from handlers.reg.reg_description import reg_description_router
from handlers.reg.reg_purposes import reg_purposes_router
from handlers.reg.reg_sexf import reg_sexf_router
from handlers.reg.reg_age_min import reg_age_min_router
from handlers.reg.reg_age_max import reg_age_max_router
from handlers.profile import profile_router
from handlers.commands import commands_router
from handlers.profile_settings.prs_name import prs_name_router
from handlers.profile_settings.prs_bdate import prs_bdate_router
from handlers.profile_settings.prs_sex import prs_sex_router
from handlers.profile_settings.prs_purposes import prs_purposes_router
from handlers.profile_settings.prs_geo import prs_geo_router
from handlers.profile_settings.prs_description import prs_description_router
from handlers.profile_settings.prs_photos import prs_photos_router
from handlers.profile_settings.prs_sex_f import prs_sex_f_router
from handlers.profile_settings.prs_age_f import prs_age_f_router
from handlers.profile_settings.prs_deactivate import prs_deactivate_router
from handlers.reg.reg_tg_id import reg_tg_id_router
from handlers.search_engine import search_engine_router
from handlers.match_engine import match_engine_router
from handlers.profile_settings.prmd_height import prmd_height_router
from handlers.profile_settings.prmd_hobby import prmd_hobby_router
from handlers.profile_settings.prmd_habits import prmd_habits_router
from handlers.profile_settings.prmd_animals import prmd_animals_router
from handlers.profile_settings.prmd_children import prmd_children_router
from handlers.profile_settings.prmd_busy import prmd_busy_router
from handlers.profile_settings.prs_km_f import prs_km_f_router
from handlers.complaints.category import comp_cat_router
from handlers.complaints.description import comp_desc_router
from handlers.complaints.confirm import comp_confirm_router
from handlers.report import report_router