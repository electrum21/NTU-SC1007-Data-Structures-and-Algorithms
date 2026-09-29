    if not current or not current.next:
            print("Index out of range")
            return False
        
        temp = current.next
        current.next = temp.next
        del temp
        ll.size -= 1
        return True