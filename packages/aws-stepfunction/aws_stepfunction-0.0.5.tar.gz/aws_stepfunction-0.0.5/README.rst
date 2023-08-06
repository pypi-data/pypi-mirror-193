
.. image:: https://readthedocs.org/projects/aws_stepfunction/badge/?version=latest
    :target: https://aws_stepfunction.readthedocs.io/index.html
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/aws_stepfunction-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/aws_stepfunction-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/aws_stepfunction-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/aws_stepfunction-project

.. image:: https://img.shields.io/pypi/v/aws_stepfunction.svg
    :target: https://pypi.python.org/pypi/aws_stepfunction

.. image:: https://img.shields.io/pypi/l/aws_stepfunction.svg
    :target: https://pypi.python.org/pypi/aws_stepfunction

.. image:: https://img.shields.io/pypi/pyversions/aws_stepfunction.svg
    :target: https://pypi.python.org/pypi/aws_stepfunction

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/aws_stepfunction-project

------


.. image:: https://img.shields.io/badge/Link-Document-green.svg
    :target: https://aws_stepfunction.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://aws_stepfunction.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://aws_stepfunction.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/aws_stepfunction-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/aws_stepfunction-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/aws_stepfunction-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/aws_stepfunction#files


Welcome to ``aws_stepfunction`` Documentation
==============================================================================
.. note::

    You may not viewing the full document, `FULL DOCUMENT IS HERE <https://aws-stepfunction.readthedocs.io/index.html>`_

**Why this Library?**

``aws_stepfunction`` provides AWS StepFunction developer a "smooth", "interruption free", "enjoyable" development experience.

If your mind set matches most of the following, ``aws_stepfunction`` is the right tool for you:

- I love the AWS StepFunction Visual Editor
- I love Python
- I don't want to spent much time learning the Amazon State Machine JSON DSL (Domain Specific Language)
- I can't memorize the code syntax
- I respect code readability and maintainability

**Talk is cheap, show me the code**

The following code snippet is an equivalent of the below Workflow in the Visual Editor

.. code-block:: python

    import aws_stepfunction as sfn
    from boto_session_manager import BotoSesManager

    # Declare a workflow object
    workflow = sfn.Workflow(comment="The power of aws_stepfunction library!")

    # Define some tasks and states
    task_invoke_lambda = sfn.actions.lambda_invoke(func_name="stepfunction_quick_start")
    succeed = sfn.Succeed()
    fail = sfn.Fail()

    # Orchestrate the Workflow
    (
        workflow.start_from(task_invoke_lambda)
        .choice([
            (  # define condition
                sfn.not_(sfn.Var("$.body").string_equals("failed!"))
                .next_then(succeed)
            ),
            (  # define condition
                sfn.Var("$.body").string_equals("failed!")
                .next_then(fail)
            ),
        ])
    )

    # Declare an instance of State Machine
    state_machine = sfn.StateMachine(
        name="stepfunction_quick_start",
        workflow=workflow,
        role_arn="arn:aws:iam::111122223333:role/my_lambda_role",
    )

    # Deploy state machine
    bsm = BotoSesManager(profile_name="my_aws_profile", region_name="us-east-1")
    state_machine.deploy(bsm)

    # Execute state machine with custom payload
    state_machine.execute(bsm, payload={"name": "alice"})

    # delete step function
    state_machine.delete(bsm)

.. image:: https://user-images.githubusercontent.com/6800411/183264808-ecf1c7bc-0c9a-40fd-a42d-ea06e472c9ec.png
    :width: 800

**You mentioned "Smooth Development Experiment"?**

I guess "a picture is worth a thousand words":

.. image:: https://user-images.githubusercontent.com/6800411/183265960-5c1b3e15-e3ac-4035-a8f3-b39d4810e466.png
    :width: 600

.. image:: https://user-images.githubusercontent.com/6800411/183265961-9312df74-9fbe-42b3-bfc8-747ce0009929.png
    :width: 600

.. image:: https://user-images.githubusercontent.com/6800411/183265962-c01bc5d4-7d0a-40a2-9a6a-0207a12b41cb.png
    :width: 600

.. image:: https://user-images.githubusercontent.com/6800411/183265963-8d177efb-93a9-484a-856a-cc2d6f7c4d15.png
    :width: 600


.. _install:

Install
------------------------------------------------------------------------------

``aws_stepfunction`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install aws_stepfunction

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade aws_stepfunction
