from quick_plot_helper import quick_plot

twocolordoulbe = ['tab:blue', 'tab:orange', 'tab:blue', 'tab:orange',]
twosoliddashed = ['dashed', 'dashed',  'solid', 'solid', ]
threecolordoulbe = ['tab:blue', 'tab:orange', 'tab:red', 'tab:blue', 'tab:orange', 'tab:red']
threesoliddashed = ['dashed', 'dashed', 'dashed', 'solid', 'solid', 'solid', ]
standard_6_colors = ('tab:red', 'tab:orange', 'tab:blue', 'tab:brown', 'tab:pink','tab:grey')

envs = ['Hopper-v3', 'HalfCheetah-v3']
data_path = '../data/'

standard_ys = ['AverageTestEpRet', 'AverageQ1Vals', 'AverageNormQBias', 'StdNormQBias', 'Time']

plot_proj3 = True
if plot_proj3:
    quick_plot(
        [
         'SAC polyak 0', 'SAC polyak 0.9', 'SAC polyak 0.995',' SAC polyak 1'],
        [
            'exp_e300_q2_uf1_lr0.0003_g0.99_p0_ss5000_b64_h64',
            'exp_e300_q2_uf1_lr0.0003_g0.99_p0.9_ss5000_b64_h64',
            'exp_e300_q2_uf1_lr0.0003_g0.99_p0.995_ss5000_b64_h64',
            'exp_e300_q2_uf1_lr0.0003_g0.99_p1_ss5000_b64_h64'
        ],
        envs=envs,
        save_name='SAC_polyak',
        base_data_folder_path=data_path,
        y_value=standard_ys
    )

