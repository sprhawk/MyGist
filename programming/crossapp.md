#CrossApp

1. set title of view controller

    a. 

        ```c++
        FirstViewController::FirstViewController()
        {
            this->setTitle("test1");
        }


    b. 

        ```c++
        this->getNavigationBarItem()->setTitle("test2");
        this->getNavigationController()->updateItem(this);
