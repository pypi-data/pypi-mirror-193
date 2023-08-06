config = {
    'model_config': {
        'business_cell_scope_id': 2404,  # 'bc_higher', # pl_1_business_line
        'grouping_columns': [2443, 2390, 2389, 2392, 2444, 2379, 2407, 2395],
        # material_grade, material_color_text, material_packaging_text, customer, commercial_ra, pl_4_product_line
        'lower_b': 0,
        'upper_b': 100,
        'mult': 5,
        'rolling_year': ['2023'],  # representation: rolling_year
        'separate_run_per_ry': True,
        'model_fit_level_scope_id': 2407,  # 'product_level', # pl_4_product_line
        'model_factor_input_scope_id': 2390,  # 'product'
        'drivers_id': [
            {
                "business_cell": "PERFORMANCE POLYMERS",
                "drivers": [
                    {"scope_id": 2379, "threshold": 0}, {"scope_id": 2389, "threshold": 2},
                    {"scope_id": 2392, "threshold": 0},
                ]
            },
            {
                "business_cell": "SPECIALTIES",
                "drivers": [
                    {"scope_id": 2379, "threshold": 0}, {"scope_id": 2389, "threshold": 2},
                    {"scope_id": 2395, "threshold": 2}, {"scope_id": 2392, "threshold": 0},
                ]
            }
        ]
    }
}
