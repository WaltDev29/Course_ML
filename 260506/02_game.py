TOTAL = 3
M = 0
C = 1
ground = [[0,0], [TOTAL, TOTAL]]
boat_side = 1 # 0: left, 1: right
side_str = ["왼쪽", "오른쪽"]

is_game_over = False
is_clear = False

while True:
    # ============ 상태 출력 및 입력 ============
    print(f"선교사 {ground[0][M]} | 식인종 {ground[0][C]}\t\t선교사 {ground[1][M]} | 식인종 {ground[1][C]}")
    print(f"배 위치: {side_str[boat_side]}")

    onboarding = list(map(int, input("command: ").split()))
    print()



    # ============ 예외 처리 ============
    if len(onboarding) != 2 or sum(onboarding) > 2:
        print("최대 두 명까지 탑승할 수 있습니다. (예: 1 1)")
        continue

    if onboarding[0] + onboarding[1] <= 0:
        print("최소 한 명은 배에 탑승해야 합니다.")
        continue

    if onboarding[0] < 0 or onboarding[1] < 0:
        print("음수 입력은 불가능합니다.")
        continue

    if onboarding[M] > ground[boat_side][M] or onboarding[C] > ground[boat_side][C]:
        print(f"{side_str[boat_side]}에 해당 인원이 없습니다.")
        continue



    # ============ 탑승 ============
    ground[boat_side][M] -= onboarding[M]
    ground[boat_side][C] -= onboarding[C]
    boat_side = abs(1 - boat_side)



    # ============ 이동 ============
    ground[boat_side][M] += onboarding[M]
    ground[boat_side][C] += onboarding[C]



    # ============ 게임 오버 체크 ============
    if (ground[0][M] > 0 and ground[0][M] < ground[0][C]) or (ground[1][M] > 0 and ground[1][M] < ground[1][C]):
        is_game_over = True
        break



    # ============ 게임 클리어 체크 ============
    if ground[0][M] == TOTAL and ground[0][C] == TOTAL:
        is_clear = True
        break


# ============ 결과 출력 ============
if is_game_over:
    print("\n###### 게임 오버! 선교사가 잡아먹혔습니다. ######")
elif is_clear:
    print("\n###### 게임 클리어! 모두 안전하게 건넜습니다. ######")

print(f"------ 최종 상태 ------\n선교사 {ground[0][M]} | 식인종 {ground[0][C]}\t\t선교사 {ground[1][M]} | 식인종 {ground[1][C]}")