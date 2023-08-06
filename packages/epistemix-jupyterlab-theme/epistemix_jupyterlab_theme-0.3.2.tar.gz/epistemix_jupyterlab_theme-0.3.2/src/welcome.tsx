import React from 'react';
import { JupyterFrontEnd } from '@jupyterlab/application';
import { ICommandPalette, ReactWidget } from '@jupyterlab/apputils';
import { notificationList } from './notifications';

class ExampleWidget extends ReactWidget {
  constructor() {
    super();
    this.addClass('welcome-widget');
    this.addClass('jp-RenderedHTMLCommon');
    this.id = 'welcome-widget';
    this.title.label = 'Welcome';
    this.title.closable = true;
    this.title.iconClass = 'fa fa-door-open';
  }

  render() {
    return (
      <div className="welcome-widget-content">
        <div className="inner">
          <h1>Welcome to the Epistemix Platform!</h1>
          <p>
            The Epistemix Platform is a web-based IDE that will enable you to
            design, run, and analyze agent-based models with FRED, the Framework
            for Reconstructing Epidemiological Dynamics.
          </p>
          <h2>Getting Started</h2>
          <p>
            On the left of the screen, you will find your home folder, as well
            as the files in your current working directory. We've pre-populated
            it with reference material that we think you will find useful!
          </p>
          <h4>Quickstart Guide</h4>
          <p>
            Start here! This guide contains lessons that will give you a
            high-level overview of many of FRED's features, and walk you through
            the process of creating a model.
          </p>
          <h4>Introductory Models</h4>
          <p>
            The introductory models directory contains examples of models that
            we feel provide good visualization of the types of behaviors and
            problems that FRED can simulate, along with some accompanying
            explanatory text that describes what each model is doing.
          </p>
          <h4>Demo Models</h4>
          <p>
            The demo models directory contains more examples of models used to
            simulate behavior in a variety of real-world situations.
          </p>
          <h4>Reset Guides</h4>
          <p>
            We've added a notebook that contains a cell allowing you to reset
            all of the guides described above. This lets you to play with the
            models themselves without fear of breaking them.
          </p>
          <h2>Additional Resources</h2>
          <ul>
            <li>
              <a href="https://docs.epistemix.com/">Documentation Home Page</a>
            </li>
            <li>
              <a href="https://epistemix.discourse.group/">Discourse Forum</a>
            </li>
            <li>
              <a href="https://blog.epistemix.com/blog/">Blog</a>
            </li>
          </ul>
          <p>
            For any other questions, please email{' '}
            <a href="mailto:learning@epistemix.com">learning@epistemix.com</a>.
          </p>
          <h2>Things to Note</h2>
          <p>
            Changes made to the contents of the Quickstart Guide and other
            pre-populated folders are not considered persistent. Updates to the
            guides can cause any changes that you've made to them to be
            overwritten. When writing a model, ensure that you are not working
            in a subdirectory of any of the existing guides.
          </p>
          <p>
            <i>
              Tip: To reopen this page, open the command palette (
              <kbd>Shift</kbd> + <kbd>CMD/CTRL</kbd> + <kbd>C</kbd>) and search
              "Open Welcome Page".
            </i>
          </p>
          <h2>Latest Updates</h2>
          <ul className="welcome-notifications">
            {notificationList.map(n => {
              return (
                <li key={n.date}>
                  <i className="notification-date">{n.date}</i>
                  <div dangerouslySetInnerHTML={{ __html: n.description }} />
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    );
  }
}

export function registerWelcomePage(
  app: JupyterFrontEnd,
  palette: ICommandPalette
): void {
  const command = 'welcome-page:open';

  const createCommand = () => {
    const widget = new ExampleWidget();
    app.shell.add(widget, 'main');
  };

  app.restored.then(() => {
    const widgets = app.shell.widgets('main');
    if (!widgets.next()) {
      createCommand();
    }
  });

  app.commands.addCommand(command, {
    label: 'Open Welcome Page',
    execute: () => {
      createCommand();
    }
  });

  palette.addItem({ command, category: 'my-category' });
}
