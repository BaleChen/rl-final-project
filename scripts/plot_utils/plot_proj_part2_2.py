from quick_plot_helper import quick_plot

twocolordoulbe = ['tab:blue', 'tab:orange', 'tab:blue', 'tab:orange',]
twosoliddashed = ['dashed', 'dashed',  'solid', 'solid', ]
threecolordoulbe = ['tab:blue', 'tab:orange', 'tab:red', 'tab:blue', 'tab:orange', 'tab:red']
threesoliddashed = ['dashed', 'dashed', 'dashed', 'solid', 'solid', 'solid', ]
standard_6_colors = ('tab:red', 'tab:orange', 'tab:blue', 'tab:brown', 'tab:pink','tab:grey')

envs = ['Hopper-v3', 'HalfCheetah-v3']
data_path = '../data/'

standard_ys = ['AverageTestEpRet', 'AverageQ1Vals', 'AverageNormQBias', 'StdNormQBias', 'Time']

proj_part2_2 = True
if proj_part2_2:
    quick_plot(
        [
         # 'Default SAC',
         # 'SAC with REDQ',
         'SAC with reset',
         'SAC with REDQ and reset'],
        [
            # 'exp_e300_q2_uf32_lr0.0003_g0.99_p0.995_ss5000_b128_h128_rs0',
            # 'exp_e300_q10_uf32_lr0.0003_g0.99_p0.995_ss5000_b128_h128_rs0',
            'exp_e300_q2_uf32_lr0.0003_g0.99_p0.995_ss5000_b128_h128_rs3',
            'exp_e300_q10_uf32_lr0.0003_g0.99_p0.995_ss5000_b128_h128_rs3'
        ],
        envs=envs,
        save_name='SAC_variants_utd32',
        base_data_folder_path=data_path,
        y_value=standard_ys
    )

