import anki_vector


def main():
    with anki_vector.Robot() as robot:
      robot.viewer.show()
      time.sleep(10)


if __name__ == "__main__":
    main()
