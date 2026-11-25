# 통계학입문 과제 2 — 단측 Z-가설검정 (Python 학생용)
# 이름: 유병우  학번: 2026191076
# 목표: Z-검정, 임계값, p-value, if/else 판단, 기각역 그래프를 작성함
# 실행 전: pip install numpy scipy matplotlib

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# [상황] 음료의 공칭 평균 용량은 500mL임.
# 36개 표본의 평균은 496mL이며, 모표준편차는 12mL로 알려져 있음.
# 실제 평균이 500mL보다 작은지 유의수준 5%에서 검정함.
# 주의: 모표준편차가 알려졌으므로 단일표본 Z-검정을 사용함.

# 문제 1. 가설을 주석으로 작성할 것
# H0: mu = 500 (실제 평균 용량은 500mL이다)
# H1: mu < 500 (실제 평균 용량은 500mL보다 작다)

mu_0 = 500
x_bar = 496
sigma = 12
n = 36
alpha = 0.05

# 문제 2. 표준오차를 계산할 것: sigma / sqrt(n)
standard_error = sigma / np.sqrt(n)  # TODO

# 문제 3. Z-검정통계량을 계산할 것: (x_bar - mu_0) / standard_error
z_stat = (x_bar - mu_0) / standard_error  # TODO

# 문제 4. 왼쪽 단측검정의 임계값을 구할 것
# stats.norm.ppf(alpha)는 왼쪽 꼬리의 면적이 alpha가 되는 지점을 반환함
critical_z = stats.norm.ppf(alpha)  # TODO

# 문제 5. 왼쪽 단측검정의 p-value를 구할 것
# stats.norm.cdf(z_stat)는 P(Z <= z_stat)을 반환함
p_value = stats.norm.cdf(z_stat)  # TODO

print('2. 표준오차:', standard_error)
print('3. Z-검정통계량:', z_stat)
print('4. 임계값:', critical_z)
print('5. p-value:', p_value)

# 문제 6. 조건문으로 결론을 작성할 것
# TODO: 아래 조건의 None을 p_value로 수정할 것
if p_value is not None:
    if p_value < alpha:
        print('귀무가설을 기각함')
    else:
        print('귀무가설을 기각하지 못함')

# 문제 7. 표준정규분포, 왼쪽 기각역, 검정통계량을 시각화할 것
# fill_between(구간, 곡선값)은 해당 부분의 아래쪽 면적을 채움
if z_stat is not None and critical_z is not None:
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x)
    plt.plot(x, y, label='Standard normal density')
    rejection_x = x[x <= critical_z]
    rejection_y = stats.norm.pdf(rejection_x)
    # TODO: 아래 줄을 완성하여 왼쪽 기각역을 음영 처리할 것
    plt.fill_between(rejection_x, rejection_y, alpha=0.3, label='Rejection region')
    # TODO: 임계값과 검정통계량에 각각 수직선을 그릴 것
    plt.axvline(critical_z, linestyle='--', label='Critical Z')
    plt.axvline(z_stat, linestyle=':', label='Observed Z')
    plt.title('Left-tailed Z test (alpha = 0.05)')
    plt.xlabel('Z')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

# 문제 8. 결과의 의미를 일상적인 언어로 2~3문장 작성할 것
# 답: 표본 36개의 평균 용량이 496mL일 때 Z-검정통계량은 -2.0으로 임계값(약 -1.645)보다 왼쪽에 위치하며, p-value(약 0.0228)도 유의수준 0.05보다 작습니다.
#     따라서 귀무가설을 기각하며, 음료의 실제 평균 용량이 표시된 500mL보다 적다고 볼 충분한 통계적 근거가 있습니다.
#     즉, 표본에서 나타난 4mL의 차이는 단순한 우연보다는 실제 평균 용량 부족 때문일 가능성이 높습니다.