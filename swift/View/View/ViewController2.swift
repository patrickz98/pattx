//
//  ViewController2.swift
//  View
//
//  Created by patrick zierahn on 12.06.15.
//  Copyright (c) 2015 patrick zierahn. All rights reserved.
//

import UIKit

class ViewController2: UIViewController {
    
    @IBOutlet weak var Zurueck: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func backPres(sender: AnyObject) {
//        self.navigationController?.popViewControllerAnimated(true)
//        self.navigationController?.popToRootViewControllerAnimated(true)
        self.dismissViewControllerAnimated(true, completion: nil)

        println("test")
    }
}
