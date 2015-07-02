//
//  ViewController.swift
//  View
//
//  Created by patrick zierahn on 13.06.15.
//  Copyright (c) 2015 patrick zierahn. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var Button1: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func Button1Pres(sender: AnyObject) {
        
//        let view2 = self.storyboard?.instantiateViewControllerWithIdentifier("View2") as! ViewController2
//        self.navigationController!.pushViewController(view2, animated: true)
        
//        let secondViewController:ViewController2 = ViewController2()
//        self.presentViewController(secondViewController, animated: true, completion: nil)
        
        self.performSegueWithIdentifier("View2", sender: nil)
        println("test")

    }

}

