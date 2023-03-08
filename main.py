from python_file import (parse_cmd
                        , add_friend_user 
                        , init_session 
                        , output_data 
                        )


def main():

    API_V = 5.135

    
    try:
        vk = init_session.init_session()
    except Exception as e:
        print(f'Something went wrong with creating a session by token: {e}')

    args = parse_cmd.parse_cmd()
    if not args.id:
        print("Argument ID missed!")
        return 1


    friend_list = add_friend_user.add_friend_user(vk, args.id)
    if friend_list:
       output_data.output_data( friend_list, args.id, args.extension, args.path)        
    else:
        print(f'https://vk.com/id{args.id} has no friends')
        return 1
    

if __name__ == '__main__':
    main()