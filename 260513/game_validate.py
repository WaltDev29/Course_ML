def play_game(command:list[list[int]]):
    CHANCE = 20
    TOTAL = 3
    M = 0
    C = 1
    ground = [[0,0], [TOTAL, TOTAL]]
    boat_side = 1 # 0: left, 1: right
    side_str = ["왼쪽", "오른쪽"]

    is_game_over = False
    is_clear = False

    print("\n\n============ 게임 시작! ============")
    count = 0
    while True:
        count += 1
        if count > CHANCE or len(command) == 0:
            is_game_over = True
            break
        # ============ 상태 출력 및 입력 ============
        print(f"선교사 {ground[0][M]} | 식인종 {ground[0][C]}\t\t선교사 {ground[1][M]} | 식인종 {ground[1][C]}")
        print(f"배 위치: {side_str[boat_side]}")

        onboarding = command.pop(0)
        print(f"입력: {onboarding}\n")



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
        if count > CHANCE:
            print(f"\n###### 게임 오버! {CHANCE}회 이상 시도했습니다. ######")
            pass
        else:
            print("\n###### 게임 오버! 선교사가 잡아먹혔습니다. ######")
            pass
    elif is_clear:
        print("\n###### 게임 클리어! 모두 안전하게 건넜습니다. ######")
        pass

    print(f"------ 최종 상태 ------\n선교사 {ground[0][M]} | 식인종 {ground[0][C]}\t\t선교사 {ground[1][M]} | 식인종 {ground[1][C]}")


    fitness = 0

    # 왼쪽으로 이동한 사람 수
    fitness += (ground[0][M] + ground[0][C]) * 50

    # 이동 횟수 패널티
    fitness -= count * 3

    # 게임오버 패널티
    if is_game_over:
        fitness -= 100

    # 클리어 보너스
    if is_clear:
        fitness += 1000

    return fitness, count


if __name__ == "__main__":
    command = [[0, 2], [0, 1], [0, 2], [0, 1], [2, 0], [1, 1], [2, 0], [0, 1], [0, 2], [0, 1], [0, 2], [0, 2], [2, 0], [0, 2], [1, 1]]
    fitness, count = play_game(command)
    print(f"최종 적합도: {fitness}")
    print(f"시도 횟수: {count}")