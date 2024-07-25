def devide_tone(target):
    tones = {'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'}
    result = []
    i = 0
    while i < len(target):
        if i + 2 <= len(target) and target[i:i + 2] in tones:
            result.append(target[i:i + 2])
            i += 2
        elif i + 1 <= len(target) and target[i] in tones:
            result.append(target[i])
            i += 1
        else:
            i += 1
    return result


def solution(m, musicinfos):
    answer = []
    m_lst = devide_tone(m)
    m_lst_len = len(m_lst)
    print('m_lst', m_lst)
    for index, ele in enumerate(musicinfos):
        start, end, title, music = ele.split(',')
        si = int(str(start)[:2]) * 60 + int(str(start[3:]))
        ei = int(str(end)[:2]) * 60 + int(str(end[3:]))
        music_lst = devide_tone(music)
        music_len = len(music_lst)
        expand_music_lst = music_lst * ((ei - si + 1) // music_len) \
                           + music_lst[:((ei - si + 1) % music_len)]
        # print('music_lst', music_lst)
        # print('expand_music_lst', expand_music_lst)

        cursor = 0
        for i in range(len(expand_music_lst) - m_lst_len):
            if expand_music_lst[i:i+m_lst_len] == m_lst:
                answer.append((title, ei - si, index))
                break

    # print('answer', answer)
    return sorted(answer, key=lambda x: (-x[1], x[2]))[0][0] if len(answer) > 0 else "(None)"